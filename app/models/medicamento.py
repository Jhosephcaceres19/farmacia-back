from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.proveedor import Proveedor  # Asegúrate de importar el modelo


class Medicamento(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    nombremedicamento = Column(String(100), nullable=False)
    medicamentocontrolado = Column(Boolean, nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    cantidad = Column(Integer, nullable=False)
    lote = Column(String(50), nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    detalle = Column(String(255), nullable=True)
    proveedor_id = Column(Integer, ForeignKey('proveedores.id'))
    proveedor = relationship("Proveedor", back_populates="medicamentos")  # Agregar esta relación

    detalles = relationship("DetalleFactura", back_populates="medicamento")
