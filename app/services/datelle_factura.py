from sqlalchemy.orm import Session
from app.models.detalle_factura import DetalleFactura
from app.schemas.detalle_factura import DetalleFacturaCreate

def get_detalle_factura(db: Session, detalle_factura_id: int):
    return db.query(DetalleFactura).filter(DetalleFactura.id == detalle_factura_id).first()

def get_detalles_factura(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetalleFactura).offset(skip).limit(limit).all()

def create_detalle_factura(db: Session, detalle_factura: DetalleFacturaCreate):
    db_detalle_factura = DetalleFactura(**detalle_factura.dict())
    db.add(db_detalle_factura)
    db.commit()
    db.refresh(db_detalle_factura)
    return db_detalle_factura
