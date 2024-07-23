from typing import Optional, Tuple
from src.domain.model.weelky_monitoring_model import WeeklyMonitoring
from src.domain.port.weekly_monitoring_interface import WeeklyMonitoringInterface
from src.domain.model.health_model import Health
from fastapi import File, UploadFile, HTTPException

class CreateWeeklyMonitoringUseCase:
    def __init__(self, repository: WeeklyMonitoringInterface):
        self.repository = repository
        
    async def execute(self, file: UploadFile, id_user: int, id_cattle: int,
                                       age: int, weight: float, water_consumption: int,
                                       food_consumption: int, behavior: int) -> Tuple[WeeklyMonitoring, Health]:
        try:
            created_object, new_health = await self.repository.create_weekly_monitoring(file, id_user, id_cattle, age, weight, water_consumption, food_consumption, behavior)
            return created_object, new_health
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e