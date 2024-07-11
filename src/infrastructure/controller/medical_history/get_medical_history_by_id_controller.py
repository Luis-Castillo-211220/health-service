from fastapi import HTTPException
from typing import Optional
from src.domain.model.medical_history_model import MedicalHistory
from src.application.medical_history.get_medical_history_by_id_use_case import GetMedicalHistoryByIdUseCase

class GetMedicalHistoryByIdController:
    def __init__(self, get_medical_history_by_id_use_case: GetMedicalHistoryByIdUseCase):
        self.get_medical_history_by_id_use_case = get_medical_history_by_id_use_case

    async def run(self, medical_history_id: int) -> Optional[MedicalHistory]:
        try:
            medical_history = await self.get_medical_history_by_id_use_case.execute(medical_history_id)
            if medical_history:
                return medical_history
            else:
                raise HTTPException(status_code=404, detail="Medical history not found.")
        except Exception as e:
            print("Error in GetMedicalHistoryByIdController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while fetching medical history.")