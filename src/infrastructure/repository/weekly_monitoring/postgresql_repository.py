from fastapi import UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import Optional, Tuple
from src.domain.entity.weekly_monitoring import WeeklyMonitoring as WeeklyMonitoringEntity
from src.domain.model.weelky_monitoring_model import WeeklyMonitoring, WeeklyMonitoringCreate
from src.domain.port.weekly_monitoring_interface import WeeklyMonitoringInterface
from inference_sdk import InferenceHTTPClient
import os
import tempfile
from datetime import datetime
from src.domain.model.health_model import Health as HealthModel
from src.domain.model.health_model import HealthCreate
from src.domain.entity.health import Health as HealthEntity
from src.infrastructure.utils.predict import predecir_salud

class PostgresqlWeeklyMonitoringRepository(WeeklyMonitoringInterface):
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_weekly_monitoring(self, file: UploadFile, id_user: int, id_cattle: int, age: int, weight: float, water_consumption: int, food_consumption: int, behavior: int) -> Tuple[WeeklyMonitoring, HealthModel]:
        try:
            CLIENT = InferenceHTTPClient(
                api_url="https://classify.roboflow.com",
                api_key="qKfcXB2ZPSHBHWzCSVHO"
            )
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                tmp.write(await file.read())
                tmp_path = tmp.name
            
            result = CLIENT.infer(tmp_path, model_id="cattle-diseases/1")

            os.remove(tmp_path)
            
            if not result:
                raise HTTPException
            
            general_health = result.get("predictions", {}).get("healthy", {}).get("confidence", None)
            general_health_percentage = round(general_health * 100, 2)
            
            if not general_health:
                return print("ERROR in post API")   
            
            createdItem = WeeklyMonitoringCreate(id_user=id_user, id_cattle=id_cattle, age=age, weight=weight, water_consumption=water_consumption,
                                                food_consumption=food_consumption, behavior=behavior, general_health=general_health_percentage)
            
            db_weekly_monitoring = WeeklyMonitoringEntity(**createdItem.dict())
            
            self.db.add(db_weekly_monitoring)
            await self.db.commit()
            await self.db.refresh(db_weekly_monitoring)
            
            prediccion = predecir_salud(age, weight, water_consumption, food_consumption, behavior, general_health_percentage)
            
            existhealth = await self.db.execute(select(HealthEntity).filter_by(id_user=id_user, id_cattle=id_cattle))
            existing_prediction = existhealth.scalar_one_or_none()
            
            if existing_prediction:
                existing_prediction.date = datetime.utcnow()
                existing_prediction.percentage_health = prediccion
                await self.db.commit()
                await self.db.refresh(existing_prediction)
                health = HealthModel.from_orm(existing_prediction)
            else:
                new_prediction = HealthCreate(
                    id_user=id_user,
                    id_cattle=id_cattle,
                    date=datetime.utcnow(),
                    percentage_health=prediccion
                )
                db_health = HealthEntity(**new_prediction.dict())
                self.db.add(db_health)
                await self.db.commit()
                await self.db.refresh(db_health)
                health = HealthModel.from_orm(db_health)
                
            return WeeklyMonitoring.from_orm(db_weekly_monitoring), health
        except Exception as e:
            print("Error in PostgresqlWeeklyMonitoringRepository:", e)
            raise HTTPException(status_code=500, detail=str(e)) from e