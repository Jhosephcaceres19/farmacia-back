from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.usuario import Usuario

class Factura(Base):
    __tablename__ = "factura"
    id = Column(Integer, primary_key=True, index=True)
    nombrecliente = Column(String, nullable=False)
    documento = Column(String, nullable=False)
    tipode_documento = Column(String, nullable=False)
    tipo_comprobante = Column(String, nullable=False)
    numerofactura = Column(String, unique=True, nullable=False)
    total = Column(Float, nullable=False)
    recibi_int = Column(Integer, nullable=False)
    ca = Column(Integer, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="facturas")

    detalles = relationship("DetalleFactura", back_populates="factura")
