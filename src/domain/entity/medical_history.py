from sqlalchemy import Column, Integer, JSON, String
from src.database.mysql import Base

class MedicalHistory(Base):
    __tablename__ = 'medical_history'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_user = Column(Integer, nullable=False)
    id_cattle = Column(Integer, nullable=False)
    vaccunate_dates = Column(JSON, nullable=False)
    past_diseases = Column(JSON, nullable=False)
    weight = Column(Integer, nullable=False)
    breed = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
