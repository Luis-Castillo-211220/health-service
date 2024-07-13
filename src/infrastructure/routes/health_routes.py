from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.domain.model.health_model import Health, HealthCreate
from src.infrastructure.controller.health.create_health_controller import CreateHealthController
from src.infrastructure.controller.health.get_health_by_user_and_cattle_controller import GetHealthByUserAndCattleController
from src.infrastructure.dependencies.health_dependencies import (
    create_health_controller,
    get_health_by_user_and_cattle_controller
)

router = APIRouter()

@router.post("/health/", response_model=Health)
async def create_health(health: HealthCreate, controller: CreateHealthController = Depends(create_health_controller)):
    try:
        return await controller.run(health)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.get("/health/{id_user}/{id_cattle}", response_model=Health)
async def get_health_by_user_and_cattle(id_user: int, id_cattle: int, controller: GetHealthByUserAndCattleController = Depends(get_health_by_user_and_cattle_controller)):
    try:
        return await controller.run(id_user, id_cattle)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e