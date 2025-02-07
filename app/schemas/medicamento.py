from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from .detalle_factura import DetalleFactura

class MedicamentoBase(BaseModel):
    nombremedicamento: str
    medicamentocontrolado: bool
    codigo: str
    cantidad: int
    lote: str
    fecha_vencimiento: date
    precio_unitario: float
    detalle: Optional[str] = None
    proveedor_id: int

class MedicamentoCreate(MedicamentoBase):
    pass

class Medicamento(MedicamentoBase):
    id: int
    detalles: List[DetalleFactura] = []

    class Config:
        from_attributes = True
