from pydantic import BaseModel
from typing import List
from .detalle_factura import DetalleFactura

class FacturaBase(BaseModel):
    nombrecliente: str
    documento: str
    tipode_documento: str
    tipo_comprobante: str
    numerofactura: str
    total: float
    recibi_int: int
    ca: int
    usuario_id: int

class FacturaCreate(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int
    detalles: List[DetalleFactura] = []

    class Config:
        from_attributes = True
