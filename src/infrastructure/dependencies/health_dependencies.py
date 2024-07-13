from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.repository.health.mysql_repository import MySqlHealthRepository
from src.application.health.create_health_use_case import CreateHealthUseCase
from src.infrastructure.controller.health.create_health_controller import CreateHealthController
from src.application.health.get_health_by_user_and_cattle_use_case import GetHealthByUserAndCattleUseCase
from src.infrastructure.controller.health.get_health_by_user_and_cattle_controller import GetHealthByUserAndCattleController
from src.database.mysql import get_db

def mysql_health_repository(db: AsyncSession = Depends(get_db)) -> MySqlHealthRepository:
    return MySqlHealthRepository(db)

def create_health_use_case(repository: MySqlHealthRepository = Depends(mysql_health_repository)) -> CreateHealthUseCase:
    return CreateHealthUseCase(repository)

def create_health_controller(use_case: CreateHealthUseCase = Depends(create_health_use_case)) -> CreateHealthController:
    return CreateHealthController(use_case)

def get_health_by_user_and_cattle_use_case(repository: MySqlHealthRepository = Depends(mysql_health_repository)) -> GetHealthByUserAndCattleUseCase:
    return GetHealthByUserAndCattleUseCase(repository)

def get_health_by_user_and_cattle_controller(use_case: GetHealthByUserAndCattleUseCase = Depends(get_health_by_user_and_cattle_use_case)) -> GetHealthByUserAndCattleController:
    return GetHealthByUserAndCattleController(use_case)