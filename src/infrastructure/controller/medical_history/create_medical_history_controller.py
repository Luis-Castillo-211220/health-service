from fastapi import HTTPException
from src.domain.model.medical_history_model import MedicalHistoryCreate, MedicalHistory
from src.application.medical_history.create_medical_history_use_case import CreateMedicalHistoryUseCase

class CreateMedicalHistoryController:
    def __init__(self, create_medical_history_use_case: CreateMedicalHistoryUseCase):
        self.create_medical_history_use_case = create_medical_history_use_case

    async def run(self, medical_history: MedicalHistoryCreate) -> MedicalHistory:
        try:
            created_medical_history = await self.create_medical_history_use_case.execute(medical_history)
            if created_medical_history:
                return created_medical_history
            else:
                raise HTTPException(status_code=400, detail="Failed to create medical history.")
        except Exception as e:
            print("Error in CreateMedicalHistoryController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while creating medical history.")
