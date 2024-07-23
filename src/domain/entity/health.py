from sqlalchemy import Column, Integer, String, Float, DateTime
# from src.database.mysql import Base
from src.database.postgresql import Base
from datetime import datetime
class Health(Base):
    __tablename__ = 'health'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    id_user = Column(Integer, nullable=False)
    id_cattle = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow,nullable=False)
    percentage_health = Column(Float, nullable=False)