from pydantic import BaseModel

class DetalleFacturaBase(BaseModel):
    factura_id: int
    medicamento_id: int
    cantidad: int
    precio_unitario: float

class DetalleFacturaCreate(DetalleFacturaBase):
    pass

class DetalleFactura(DetalleFacturaBase):
    id: int

    class Config:
        from_attributes = True
