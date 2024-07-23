from fastapi import HTTPException
from src.application.weekly_monitoring.create_weekly_monitoring_use_case import CreateWeeklyMonitoringUseCase
from src.domain.model.weelky_monitoring_model import WeeklyMonitoring
from src.domain.model.health_model import Health
from fastapi import UploadFile
from typing import Tuple, Optional

class CreateWeeklyMonitoringController:
    def __init__(self, create_weekly_monitoring_use_case: CreateWeeklyMonitoringUseCase):
        self.create_weekly_monitoring_use_case = create_weekly_monitoring_use_case
        
    async def run(self, file: UploadFile, id_user: int, id_cattle: int, 
                  age: int, weight: float, water_consumption: int, 
                  food_consumption: int, behavior: int) -> Tuple[Optional[WeeklyMonitoring], Optional[Health]]:
        try:
            created_weekly_monitoring, new_health = await self.create_weekly_monitoring_use_case.execute(file, id_user, id_cattle, age, weight, water_consumption, food_consumption, behavior)
            if created_weekly_monitoring and new_health:
                return created_weekly_monitoring, new_health
            else:
               raise HTTPException (status_code=500, detail="Failed to create weekly monitoring.")
        except Exception as e:
            print("Error in CreateWeeklyMonitoringController:", e)
            raise HTTPException(status_code=500, detail="Failed to create weekly monitoring.") from e