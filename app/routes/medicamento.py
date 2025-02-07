from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.medicamento import Medicamento, MedicamentoCreate
from app.services.medicamento import get_medicamento, get_medicamentos, create_medicamento
from typing import List


router = APIRouter()

@router.post("/", response_model=Medicamento)
def create_medicamento_route(medicamento: MedicamentoCreate, db: Session = Depends(get_db)):
    return create_medicamento(db=db, medicamento=medicamento)

@router.get("/{medicamento_id}", response_model=Medicamento)
def read_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    db_medicamento = get_medicamento(db, medicamento_id=medicamento_id)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return db_medicamento

@router.get("/", response_model=List[Medicamento])
def read_medicamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medicamentos = get_medicamentos(db, skip=skip, limit=limit)
    return medicamentos
