from pydantic import BaseModel
from typing import List
from .medicamento import Medicamento

class ProveedorBase(BaseModel):
    nombre: str
    telefono: str
    direccion: str
    correoelectronico: str

class ProveedorCreate(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    id: int
    medicamentos: List[Medicamento] = []

    class Config:
        from_attributes = True
