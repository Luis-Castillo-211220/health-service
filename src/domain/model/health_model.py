from pydantic import BaseModel, field_validator, Field
from typing import Optional
from datetime import datetime

class HealthBase(BaseModel):
    id_user: int
    id_cattle: int
    date: datetime
    percentage_health: float
    
    @field_validator('percentage_health', mode='before')
    @classmethod
    def must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Deben de ser valores positivos')
        return value
    
class HealthCreate(HealthBase):
    pass

class Health(HealthBase):
    id: int
    
    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }