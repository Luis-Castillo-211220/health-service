from pydantic import BaseModel, field_validator
from datetime import datetime

class WeeklyMonitoringBase(BaseModel):
    id_user: int
    id_cattle: int
    age: int
    weight: float
    water_consumption: int
    food_consumption: int
    behavior: int
    general_health: float
    
    @field_validator('general_health', 'age', 'weight', mode='before')
    @classmethod
    def must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Deben de ser valores positivos')
        return value

class   WeeklyMonitoringCreate(WeeklyMonitoringBase):
    pass

class WeeklyMonitoring(WeeklyMonitoringBase):
    id: int
    # date: datetime
    
    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }