from fastapi import HTTPException
from typing import Optional
from src.application.health.get_health_by_user_and_cattle_use_case import GetHealthByUserAndCattleUseCase
from src.domain.model.health_model import Health

class GetHealthByUserAndCattleController:
    def __init__(self, get_health_by_user_and_cattle_use_case: GetHealthByUserAndCattleUseCase):
        self.get_health_by_user_and_use_case = get_health_by_user_and_cattle_use_case
    
    async def run(self, id_user: int, id_cattle: int) -> Optional[Health]:
        try:
            health = await self.get_health_by_user_and_use_case.execute(id_user, id_cattle)
            if health:
                return health
            else:
                raise HTTPException(status_code=404, detail="Health not found.")
        except Exception as e:
            print("Error in GetHealthByUserAndCattleController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while getting health.") from e