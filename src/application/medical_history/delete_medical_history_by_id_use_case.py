from src.domain.port.medical_history_interface import MedicalHistoryInterface

class DeleteMedicalHistoryByIdUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, medical_history_id: int) -> bool:
        return await self.repository.delete_medical_history_by_id(medical_history_id)
