from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from typing import Optional, List
from src.domain.entity.medical_history import MedicalHistory as MedicalHistoryEntity
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class MysqlMedicalHistoryRepository(MedicalHistoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_medical_history(self, medical_history: MedicalHistoryCreate) -> Optional[MedicalHistory]:
        try:
            db_medical_history = MedicalHistoryEntity(**medical_history.dict())
            self.db.add(db_medical_history)
            await self.db.commit()
            await self.db.refresh(db_medical_history)
            return MedicalHistory.model_validate(db_medical_history)
        except Exception as e:
            print("Error creating Medical History:", e)
            return None

    async def list_medical_histories(self, skip: int = 0, limit: int = 100) -> List[MedicalHistory]:
        try:
            result = await self.db.execute(select(MedicalHistoryEntity).offset(skip).limit(limit))
            medical_histories = result.scalars().all()
            return [MedicalHistory.model_validate(mh) for mh in medical_histories]
        except Exception as e:
            print("Error fetching medical histories:", e)
            return []
        
    async def get_medical_history_by_id(self, medical_history_id: int) -> Optional[MedicalHistory]:
        try:
            result = await self.db.execute(select(MedicalHistoryEntity).filter(MedicalHistoryEntity.id == medical_history_id))
            medical_history = result.scalars().first()
            if medical_history:
                return MedicalHistory.model_validate(medical_history)
            return None
        except Exception as e:
            print("Error fetching medical history by ID:", e)
            return None
        
    async def delete_medical_history_by_id(self, medical_history_id: int) -> bool:
        try:
            result = await self.db.execute(delete(MedicalHistoryEntity).where(MedicalHistoryEntity.id == medical_history_id))
            await self.db.commit()
            return result.rowcount > 0
        except Exception as e:
            print("Error deleting medical history by ID:", e)
            return False