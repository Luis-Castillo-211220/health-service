from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.domain.model.health_model import Health, HealthCreate
from src.infrastructure.controller.health.create_health_controller import CreateHealthController
from src.infrastructure.dependencies.health_dependencies import (
    create_health_controller
)

router = APIRouter()

@router.post("/health/", response_model=Health)
async def create_health(health: HealthCreate, controller: CreateHealthController = Depends(create_health_controller)):
    try:
        return await controller.run(health)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
