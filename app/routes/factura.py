from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.factura import Factura, FacturaCreate
from app.services.factura import get_factura, get_facturas, create_factura
from typing import List


router = APIRouter()

@router.post("/", response_model=Factura)
def create_factura_route(factura: FacturaCreate, db: Session = Depends(get_db)):
    return create_factura(db=db, factura=factura)

@router.get("/{factura_id}", response_model=Factura)
def read_factura(factura_id: int, db: Session = Depends(get_db)):
    db_factura = get_factura(db, factura_id=factura_id)
    if db_factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return db_factura

@router.get("/", response_model=List[Factura])
def read_facturas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    facturas = get_facturas(db, skip=skip, limit=limit)
    return facturas
