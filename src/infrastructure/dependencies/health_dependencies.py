from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.repository.health.mysql_repository import MySqlHealthRepository
from src.application.health.create_health_use_case import CreateHealthUseCase
from src.infrastructure.controller.health.create_health_controller import CreateHealthController
from src.database.mysql import get_db

def mysql_health_repository(db: AsyncSession = Depends(get_db)) -> MySqlHealthRepository:
    return MySqlHealthRepository(db)

def create_health_use_case(repository: MySqlHealthRepository = Depends(mysql_health_repository)) -> CreateHealthUseCase:
    return CreateHealthUseCase(repository)

def create_health_controller(use_case: CreateHealthUseCase = Depends(create_health_use_case)) -> CreateHealthController:
    return CreateHealthController(use_case)