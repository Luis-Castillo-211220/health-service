import random
from typing import Optional
from src.domain.model.health_model import Health, HealthCreate
from src.domain.port.health_interface import HealthInterface

class CreateHealthUseCase:
    def __init__(self, repository: HealthInterface):
        self.repository = repository
        
    async def execute(self, health: HealthCreate) -> Optional[Health]:
        try:            
            return await self.repository.create_health(health)
        except Exception as e:
            print("Error creating Health:", e)
            