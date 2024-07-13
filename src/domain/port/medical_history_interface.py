from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory

class MedicalHistoryInterface(ABC):

    @abstractmethod
    async def create_medical_history(self, medical_history: MedicalHistoryCreate) -> Optional[MedicalHistory]:
        pass
    
    @abstractmethod
    async def list_medical_histories(self, skip: int = 0, limit: int = 100) -> List[MedicalHistory]:
        pass

    @abstractmethod
    async def get_medical_history_by_id(self, medical_history_id: int) -> Optional[MedicalHistory]:
        pass

    @abstractmethod
    async def get_medical_history_by_user_and_cattle(self, id_user: int, id_cattle: int) -> Optional[MedicalHistory]:
        pass

    @abstractmethod
    async def delete_medical_history_by_id(self, medical_history_id: int) -> bool:
        pass

    @abstractmethod
    async def update_medical_history_by_id(self, medical_history_id: int, medical_history: MedicalHistory) -> Optional[MedicalHistory]:
        pass