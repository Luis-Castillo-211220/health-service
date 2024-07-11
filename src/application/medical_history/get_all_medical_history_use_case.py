from typing import List
from src.domain.model.medical_history_model import MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class ListMedicalHistoriesUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, skip: int = 0, limit: int = 100) -> List[MedicalHistory]:
        return await self.repository.list_medical_histories(skip=skip, limit=limit)
