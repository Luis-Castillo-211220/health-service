from abc import ABC, abstractmethod
from typing import Optional
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory

class MedicalHistoryInterface(ABC):

    @abstractmethod
    async def create_medical_history(self, medical_history: MedicalHistoryCreate) -> Optional[MedicalHistory]:
        pass
