from pydantic import BaseModel, field_validator
from typing import List

class MedicalHistoryBase(BaseModel):
    id_user: int
    id_cattle: int
    vaccunate_dates: List[str]
    past_diseases: List[str]
    weight: int
    breed: str
    age: int
    
    @field_validator('weight', 'age', mode='before')
    @classmethod
    def must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Deben de ser valores positivos')
        return value

class MedicalHistoryCreate(MedicalHistoryBase):
    pass

class MedicalHistory(MedicalHistoryBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True