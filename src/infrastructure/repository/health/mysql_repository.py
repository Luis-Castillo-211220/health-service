from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from src.domain.entity.health import Health as HealthEntity
from src.domain.model.health_model import Health, HealthCreate
from src.domain.port.health_interface import HealthInterface

class MySqlHealthRepository(HealthInterface):
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_health(self, health: HealthCreate) -> Optional[Health]:
        try:
            db_health = HealthEntity(**health.dict())
            self.db.add(db_health)
            await self.db.commit()
            await self.db.refresh(db_health)
            return Health.model_validate(db_health)
        except Exception as e:
            print("Error creating Health:", e)
            return None