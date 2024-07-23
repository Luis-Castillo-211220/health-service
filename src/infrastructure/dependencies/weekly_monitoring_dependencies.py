from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.postgresql import get_db
from src.infrastructure.repository.weekly_monitoring.postgresql_repository import PostgresqlWeeklyMonitoringRepository

from src.application.weekly_monitoring.create_weekly_monitoring_use_case import CreateWeeklyMonitoringUseCase
from src.infrastructure.controller.weekly_monitoring.create_weekly_monitoring_controller import CreateWeeklyMonitoringController


def postgresql_repository(db: AsyncSession = Depends(get_db)) -> PostgresqlWeeklyMonitoringRepository:
    return PostgresqlWeeklyMonitoringRepository(db)

def create_weekly_monitoring_use_case(repository: PostgresqlWeeklyMonitoringRepository = Depends(postgresql_repository)) -> CreateWeeklyMonitoringUseCase:
    return CreateWeeklyMonitoringUseCase(repository)

def create_weekly_monitoring_controller(use_case: CreateWeeklyMonitoringUseCase = Depends(create_weekly_monitoring_use_case)) -> CreateWeeklyMonitoringController:
    return CreateWeeklyMonitoringController(use_case)