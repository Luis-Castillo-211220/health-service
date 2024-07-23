from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Tuple

from src.infrastructure.controller.weekly_monitoring.create_weekly_monitoring_controller import CreateWeeklyMonitoringController
from src.domain.model.weelky_monitoring_model import WeeklyMonitoringCreate, WeeklyMonitoring
from src.domain.model.health_model import Health
from src.infrastructure.dependencies.weekly_monitoring_dependencies import (
    create_weekly_monitoring_controller
)

router = APIRouter()

@router.post("/weekly_monitoring", response_model=Tuple[WeeklyMonitoring, Health])
async def create_weekly_monitoring(file: UploadFile = File(...), id_user: int = Form(...), id_cattle: int = Form(...), age: int = Form(...), 
                                   weight: float = Form(...), water_consumption: int = Form(...), food_consumption: int = Form(...), behavior: int = Form(...),
                                   controller: CreateWeeklyMonitoringController = Depends(create_weekly_monitoring_controller)) -> Tuple[WeeklyMonitoring, Health]:
    try:
        created_weekly_monitoring, new_health = await controller.run(file, id_user, id_cattle, age, weight, water_consumption, food_consumption, behavior)
        return created_weekly_monitoring, new_health
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) 