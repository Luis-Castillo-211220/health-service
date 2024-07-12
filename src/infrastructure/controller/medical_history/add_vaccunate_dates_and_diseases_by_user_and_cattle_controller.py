from fastapi import HTTPException
from typing import List
from src.application.medical_history.add_vaccunate_dates_and_diseases_by_user_and_cattle import AddVaccunateDatesAndDiseasesByUserAndCattleUseCase
from src.domain.model.medical_history_model import MedicalHistory

class AddVaccunateDatesAndDiseasesByUserAndCattleController:
    def __init__(self, add_vaccunate_dates_and_diseases_by_user_and_cattle_use_case: AddVaccunateDatesAndDiseasesByUserAndCattleUseCase):
        self.add_vaccunate_dates_and_diseases_by_user_and_cattle_use_case = add_vaccunate_dates_and_diseases_by_user_and_cattle_use_case

    async def run(self, id_user: int, id_cattle: int, new_vaccunate_dates: List[str], new_past_diseases: List[str]) -> MedicalHistory:
        try:
            updated_medical_history = await self.add_vaccunate_dates_and_diseases_by_user_and_cattle_use_case.execute(id_user, id_cattle, new_vaccunate_dates, new_past_diseases)
            if updated_medical_history:
                return updated_medical_history
            else:
                raise HTTPException(status_code=404, detail="Medical history not found.")
        except Exception as e:
            print("Error in AddVaccunateDatesAndDiseasesByUserAndCattleController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while updating medical history.")
