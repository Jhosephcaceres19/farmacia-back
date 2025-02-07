from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.detalle_factura import DetalleFactura, DetalleFacturaCreate
from app.services.datelle_factura import get_detalle_factura, get_detalles_factura, create_detalle_factura
from typing import List


router = APIRouter()

@router.post("/", response_model=DetalleFactura)
def create_detalle_factura_route(detalle_factura: DetalleFacturaCreate, db: Session = Depends(get_db)):
    return create_detalle_factura(db=db, detalle_factura=detalle_factura)

@router.get("/{detalle_factura_id}", response_model=DetalleFactura)
def read_detalle_factura(detalle_factura_id: int, db: Session = Depends(get_db)):
    db_detalle_factura = get_detalle_factura(db, detalle_factura_id=detalle_factura_id)
    if db_detalle_factura is None:
        raise HTTPException(status_code=404, detail="Detalle de factura no encontrado")
    return db_detalle_factura

@router.get("/", response_model=List[DetalleFactura])
def read_detalles_factura(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detalles_factura = get_detalles_factura(db, skip=skip, limit=limit)
    return detalles_factura
