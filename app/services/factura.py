from sqlalchemy.orm import Session
from app.models.factura import Factura
from app.schemas.factura import FacturaCreate

def get_factura(db: Session, factura_id: int):
    return db.query(Factura).filter(Factura.id == factura_id).first()

def get_facturas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Factura).offset(skip).limit(limit).all()

def create_factura(db: Session, factura: FacturaCreate):
    db_factura = Factura(**factura.dict())
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura
