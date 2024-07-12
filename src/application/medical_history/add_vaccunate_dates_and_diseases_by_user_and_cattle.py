from typing import Optional, List
from src.domain.model.medical_history_model import MedicalHistory
from src.domain.port.medical_history_interface import MedicalHistoryInterface

class AddVaccunateDatesAndDiseasesByUserAndCattleUseCase:
    def __init__(self, repository: MedicalHistoryInterface):
        self.repository = repository

    async def execute(self, id_user: int, id_cattle: int, new_vaccunate_dates: List[str], new_past_diseases: List[str]) -> Optional[MedicalHistory]:
        # Obtener el registro existente por id_user y id_cattle
        existing_record = await self.repository.get_medical_history_by_user_and_cattle(id_user, id_cattle)
        if not existing_record:
            return None

        # Añadir nuevas fechas y enfermedades
        existing_record.vaccunate_dates.extend(new_vaccunate_dates)
        existing_record.vaccunate_dates = list(set(existing_record.vaccunate_dates))  # Eliminar duplicados
        existing_record.past_diseases.extend(new_past_diseases)
        existing_record.past_diseases = list(set(existing_record.past_diseases))  # Eliminar duplicados

        return await self.repository.update_medical_history_by_id(existing_record.id, existing_record)
