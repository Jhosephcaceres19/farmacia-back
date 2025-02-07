from pydantic import BaseModel
from typing import List
from .factura import Factura

class UsuarioBase(BaseModel):
    nombre: str
    rol: str
    ci: str
    telefono: str
    direccion: str
    correoelectronico: str
    contrasena: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    facturas: List[Factura] = []

    class Config:
        from_attributes = True
