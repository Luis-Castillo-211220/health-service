from abc import ABC, abstractmethod
from typing import Optional
from fastapi import File, UploadFile
from src.domain.model.weelky_monitoring_model import WeeklyMonitoring

class WeeklyMonitoringInterface(ABC):
    
    @abstractmethod
    async def create_weekly_monitoring(self, file: UploadFile , id_user: int, id_cattle: int,
                                       age: int, weight: float, water_consumption: int,
                                       food_consumption: int, behavior: int) -> Optional[WeeklyMonitoring]:
        pass
    
    