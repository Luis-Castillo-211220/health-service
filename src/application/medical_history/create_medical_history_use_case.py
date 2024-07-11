from typing import Optional
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class CreateMedicalHistoryUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, medical_history: MedicalHistoryCreate) -> Optional[MedicalHistory]:
        # La validación se realiza automáticamente al instanciar MedicalHistoryCreate
        return await self.repository.create_medical_history(medical_history)

