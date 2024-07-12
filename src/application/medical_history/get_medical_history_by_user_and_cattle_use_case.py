from typing import Optional
from src.domain.model.medical_history_model import MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class GetMedicalHistoryByUserAndCattleUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, id_user: int, id_cattle: int) -> Optional[MedicalHistory]:
        return await self.repository.get_medical_history_by_user_and_cattle(id_user, id_cattle)
