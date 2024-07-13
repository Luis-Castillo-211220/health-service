from typing import Optional
from src.domain.model.health_model import Health
from src.domain.port.health_interface import HealthInterface

class GetHealthByUserAndCattleUseCase:
    def __init__(self, repository: HealthInterface):
        self.repository = repository
        
    async def execute(self, id_user: int, id_cattle: int) -> Optional[Health]:
        return await self.repository.get_health_by_user_and_cattle(id_user, id_cattle)