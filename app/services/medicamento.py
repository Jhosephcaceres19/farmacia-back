from sqlalchemy.orm import Session
from app.models.medicamento import Medicamento
from app.schemas.medicamento import MedicamentoCreate

def get_medicamento(db: Session, medicamento_id: int):
    return db.query(Medicamento).filter(Medicamento.id == medicamento_id).first()

def get_medicamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Medicamento).offset(skip).limit(limit).all()

def create_medicamento(db: Session, medicamento: MedicamentoCreate):
    db_medicamento = Medicamento(**medicamento.dict())
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento
