from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class DetalleFactura(Base):
    __tablename__ = "detalle_factura"
    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer, ForeignKey('factura.id'))
    medicamento_id = Column(Integer, ForeignKey('medicamentos.id'))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    factura = relationship("Factura", back_populates="detalles")  # Este es el cambio necesario.
    medicamento = relationship("Medicamento", back_populates="detalles")  # <-- Agregar esto


