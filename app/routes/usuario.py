from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.usuario import Usuario, UsuarioCreate
from app.services.usuario import get_usuario, get_usuarios, create_usuario
from typing import List


router = APIRouter()

@router.post("/", response_model=Usuario)
def create_usuario_route(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db=db, usuario=usuario)

@router.get("/{usuario_id}", response_model=Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.get("/", response_model=List[Usuario])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = get_usuarios(db, skip=skip, limit=limit)
    return usuarios
