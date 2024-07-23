from sqlalchemy import Column, Integer, Float
from src.database.postgresql import Base

class WeeklyMonitoring(Base):
    __tablename__ = "weelky_monitoring"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    id_user = Column(Integer, nullable=False)
    id_cattle = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    water_consumption = Column(Integer, nullable=False)
    food_consumption = Column(Integer, nullable=False)
    behavior = Column(Integer, nullable=False)
    general_health = Column(Float, nullable=False)