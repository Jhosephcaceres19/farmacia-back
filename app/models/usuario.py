from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class RolEnum(enum.Enum):
    ADMIN = "admin"
    USUARIO = "usuario"
    
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    rol = Column(Enum(RolEnum), nullable=False)
    ci = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    direccion = Column(String(255), nullable=False)
    correoelectronico = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    facturas = relationship("Factura", back_populates="usuario")
