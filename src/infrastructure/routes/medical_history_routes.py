from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.domain.model.medical_history_model import MedicalHistory, MedicalHistoryCreate
from src.infrastructure.controller.medical_history.create_medical_history_controller import CreateMedicalHistoryController
from src.infrastructure.controller.medical_history.get_all_medical_history_controller import ListMedicalHistoriesController
from src.infrastructure.controller.medical_history.get_medical_history_by_id_controller import GetMedicalHistoryByIdController
from src.infrastructure.controller.medical_history.delete_medical_history_by_id_controller import DeleteMedicalHistoryByIdController
from src.infrastructure.dependencies.medical_history_dependencies import (
    get_create_medical_history_controller,
    get_list_medical_histories_controller,
    get_get_medical_history_by_id_controller,
    get_delete_medical_history_by_id_controller)

router = APIRouter()

@router.post("/medical_histories/", response_model=MedicalHistory)
async def create_medical_history(medical_history: MedicalHistoryCreate, controller: CreateMedicalHistoryController = Depends(get_create_medical_history_controller)):
    try:
        return await controller.run(medical_history)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.get("/medical_histories/", response_model=List[MedicalHistory])
async def list_medical_histories(skip: int = 0, limit: int = 100, controller: ListMedicalHistoriesController = Depends(get_list_medical_histories_controller)):
    try:
        return await controller.run(skip=skip, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
@router.get("/medical_histories/{medical_history_id}", response_model=MedicalHistory)
async def get_medical_history_by_id(medical_history_id: int, controller: GetMedicalHistoryByIdController = Depends(get_get_medical_history_by_id_controller)):
    try:
        return await controller.run(medical_history_id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.delete("/medical_histories/{medical_history_id}", response_model=bool)
async def delete_medical_history_by_id(medical_history_id: int, controller: DeleteMedicalHistoryByIdController = Depends(get_delete_medical_history_by_id_controller)):
    try:
        return await controller.run(medical_history_id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))