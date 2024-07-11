from typing import List
from fastapi import HTTPException
from src.domain.model.medical_history_model import MedicalHistory
from src.application.medical_history.get_all_medical_history_use_case import ListMedicalHistoriesUseCase

class ListMedicalHistoriesController:
    def __init__(self, list_medical_histories_use_case: ListMedicalHistoriesUseCase):
        self.list_medical_histories_use_case = list_medical_histories_use_case

    async def run(self, skip: int = 0, limit: int = 10) -> List[MedicalHistory]:
        try:
            return await self.list_medical_histories_use_case.execute(skip=skip, limit=limit)
        except Exception as e:
            print("Error in ListMedicalHistoriesController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while fetching medical histories.")
