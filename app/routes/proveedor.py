from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.proveedor import Proveedor, ProveedorCreate
from app.services.proveedor import get_proveedor, get_proveedores, create_proveedor
from typing import List


router = APIRouter()

@router.post("/", response_model=Proveedor)
def create_proveedor_route(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    return create_proveedor(db=db, proveedor=proveedor)

@router.get("/{proveedor_id}", response_model=Proveedor)
def read_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    db_proveedor = get_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return db_proveedor

@router.get("/", response_model=List[Proveedor])
def read_proveedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    proveedores = get_proveedores(db, skip=skip, limit=limit)
    return proveedores
