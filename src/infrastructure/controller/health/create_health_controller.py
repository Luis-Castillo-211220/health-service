from fastapi import HTTPException
from src.domain.model.health_model import Health, HealthCreate
from src.application.health.create_health_use_case import CreateHealthUseCase

class CreateHealthController:
    def __init__(self, create_health_use_case: CreateHealthUseCase):
        self.create_health_use_case = create_health_use_case
    
    async def run(self, health: HealthCreate) -> Health:
        try:
            created_health = await self.create_health_use_case.execute(health)
            if created_health:
                return created_health
            else:
                raise HTTPException(status_code=400, detail="Failed to create health")
        except Exception as e:
            print("Error in CreateHealthController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while creating health.")