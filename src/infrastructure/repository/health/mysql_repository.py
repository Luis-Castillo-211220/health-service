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
        
    async def get_health_by_user_and_cattle(self, id_user: int, id_cattle: int) -> Optional[Health]:
        try:
            result = await self.db.execute(select(HealthEntity).filter(HealthEntity.id_user == id_user, HealthEntity.id_cattle == id_cattle))
            health = result.scalars().first()
            if health:
                return Health.model_validate(health)
            return None
        except Exception as e:
            print("Error getting Health by user and cattle:", e)
            return None