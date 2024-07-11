from fastapi import HTTPException
from src.application.medical_history.delete_medical_history_by_id_use_case import DeleteMedicalHistoryByIdUseCase

class DeleteMedicalHistoryByIdController:
    def __init__(self, delete_medical_history_by_id_use_case: DeleteMedicalHistoryByIdUseCase):
        self.delete_medical_history_by_id_use_case = delete_medical_history_by_id_use_case

    async def run(self, medical_history_id: int) -> bool:
        try:
            result = await self.delete_medical_history_by_id_use_case.execute(medical_history_id)
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="Medical history not found.")
        except Exception as e:
            print("Error in DeleteMedicalHistoryByIdController:", e)
            raise HTTPException(status_code=500, detail="An error occurred while deleting medical history.")
