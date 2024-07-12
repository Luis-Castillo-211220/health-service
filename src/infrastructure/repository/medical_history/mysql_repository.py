from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
from typing import Optional, List
from src.domain.entity.medical_history import MedicalHistory as MedicalHistoryEntity
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class MysqlMedicalHistoryRepository(MedicalHistoryInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    #CREATE
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

    #GET ALL
    async def list_medical_histories(self, skip: int = 0, limit: int = 100) -> List[MedicalHistory]:
        try:
            result = await self.db.execute(select(MedicalHistoryEntity).offset(skip).limit(limit))
            medical_histories = result.scalars().all()
            return [MedicalHistory.model_validate(mh) for mh in medical_histories]
        except Exception as e:
            print("Error fetching medical histories:", e)
            return []
    
    #GET BY ID
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
    
    #DELETE
    async def delete_medical_history_by_id(self, medical_history_id: int) -> bool:
        try:
            result = await self.db.execute(delete(MedicalHistoryEntity).where(MedicalHistoryEntity.id == medical_history_id))
            await self.db.commit()
            return result.rowcount > 0
        except Exception as e:
            print("Error deleting medical history by ID:", e)
            return False
    
    async def get_medical_history_by_user_and_cattle(self, id_user: int, id_cattle: int) -> Optional[MedicalHistory]:
        try:
            result = await self.db.execute(select(MedicalHistoryEntity).filter(MedicalHistoryEntity.id_user == id_user, MedicalHistoryEntity.id_cattle == id_cattle))
            medical_history = result.scalars().first()
            if medical_history:
                return MedicalHistory.model_validate(medical_history)
            return None
        except Exception as e:
            print("Error fetching medical history by user and cattle:", e)
            return None
        
    async def update_medical_history_by_id(self, medical_history_id: int, medical_history: MedicalHistory) -> Optional[MedicalHistory]:
        try:
            # Actualizar el registro
            await self.db.execute(
                update(MedicalHistoryEntity)
                .where(MedicalHistoryEntity.id == medical_history_id)
                .values(**medical_history.dict(exclude_unset=True))
            )
            await self.db.commit()

            # Recuperar el registro actualizado
            result = await self.db.execute(select(MedicalHistoryEntity).filter(MedicalHistoryEntity.id == medical_history_id))
            updated_medical_history = result.scalars().first()
            if updated_medical_history:
                return MedicalHistory.model_validate(updated_medical_history)
            return None
        except Exception as e:
            print("Error updating medical history by ID:", e)
            return None