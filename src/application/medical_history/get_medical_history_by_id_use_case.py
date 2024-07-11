from typing import Optional
from src.domain.model.medical_history_model import MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class GetMedicalHistoryByIdUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, medical_history_id: int) -> Optional[MedicalHistory]:
        return await self.repository.get_medical_history_by_id(medical_history_id)
