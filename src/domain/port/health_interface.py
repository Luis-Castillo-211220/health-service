from abc import ABC, abstractmethod
from typing import Optional
from src.domain.model.health_model import HealthCreate, Health

class HealthInterface(ABC):
    
    @abstractmethod
    async def create_health(self, Health: HealthCreate) -> Optional[Health]:
        pass
    
    @abstractmethod
    async def get_health_by_user_and_cattle(self, id_user: int, id_cattle: int) -> Optional[Health]:
        pass