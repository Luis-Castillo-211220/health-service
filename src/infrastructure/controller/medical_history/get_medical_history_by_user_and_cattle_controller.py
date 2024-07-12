from fastapi import HTTPException
from typing import Optional
from src.application.medical_history.get_medical_history_by_user_and_cattle_use_case import GetMedicalHistoryByUserAndCattleUseCase
from src.domain.model.medical_history_model import MedicalHistory

class GetMedicalHistoryByUserAndCattleController:
    def __init__(self, get_medical_history_by_user_and_cattle_use_case: GetMedicalHistoryByUserAndCattleUseCase):
        self.get_medical_history_by_user_and_cattle_use_case = get_medical_history_by_user_and_cattle_use_case

    async def run(self, id_user: int, id_cattle: int) -> Optional[MedicalHistory]:
        try:
            medical_history = await self.get_medical_history_by_user_and_cattle_use_case.execute(id_user, id_cattle)
            if medical_history:
                return medical_history
            else:
                raise HTTPException(status_code=404, detail="Medical history not found.")
        except Exception as e:
            print("Error in GetMedicalHistoryByUserAndCattleController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while fetching medical history.")
