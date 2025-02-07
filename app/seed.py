from app.database import SessionLocal
from app.models.usuario import Usuario, RolEnum
from app.models.proveedor import Proveedor
from app.models.medicamento import Medicamento
from datetime import date
import random

def seed_data():
    session = SessionLocal()

    # Datos de usuarios
    usuarios = [
        {"nombre": "Juan Pérez", "rol": RolEnum.USUARIO, "ci": "12345678", "telefono": "71234567", "direccion": "Calle A #123", "correoelectronico": "juan@example.com", "contrasena": "hashed_password"},
        {"nombre": "María López", "rol": RolEnum.USUARIO, "ci": "87654321", "telefono": "76543210", "direccion": "Calle B #456", "correoelectronico": "maria@example.com", "contrasena": "hashed_password"},
        {"nombre": "Carlos Ramos", "rol": RolEnum.USUARIO, "ci": "11223344", "telefono": "70011223", "direccion": "Calle C #789", "correoelectronico": "carlos@example.com", "contrasena": "hashed_password"},
        {"nombre": "Ana Gómez", "rol": RolEnum.ADMIN, "ci": "44556677", "telefono": "78889999", "direccion": "Calle D #101", "correoelectronico": "ana@example.com", "contrasena": "hashed_password"},
        {"nombre": "Pedro Fernández", "rol": RolEnum.ADMIN, "ci": "99887766", "telefono": "79998877", "direccion": "Calle E #202", "correoelectronico": "pedro@example.com", "contrasena": "hashed_password"},
        {"nombre": "Lucía Méndez", "rol": RolEnum.ADMIN, "ci": "55443322", "telefono": "75544332", "direccion": "Calle F #303", "correoelectronico": "lucia@example.com", "contrasena": "hashed_password"},
    ]

    # Datos de proveedores
    proveedores_data = [
        {"nombre": "Farmacia La Salud", "telefono": "71234567", "direccion": "Av. Siempre Viva #123", "correoelectronico": "salud@example.com"},
        {"nombre": "Droguería San José", "telefono": "76543210", "direccion": "Calle Medicinal #456", "correoelectronico": "sanjose@example.com"},
        {"nombre": "Laboratorios Vita", "telefono": "70011223", "direccion": "Zona Industrial #789", "correoelectronico": "vita@example.com"},
        {"nombre": "Distribuidora PharmaPlus", "telefono": "78889999", "direccion": "Calle Central #101", "correoelectronico": "pharmaplus@example.com"},
    ]

    # Insertar usuarios si no existen
    for data in usuarios:
        if not session.query(Usuario).filter_by(correoelectronico=data["correoelectronico"]).first():
            usuario = Usuario(**data)
            session.add(usuario)

    # Insertar proveedores si no existen
    for data in proveedores_data:
        if not session.query(Proveedor).filter_by(correoelectronico=data["correoelectronico"]).first():
            proveedor = Proveedor(**data)
            session.add(proveedor)

    session.commit()

    # Obtener los proveedores ya insertados
    proveedores = session.query(Proveedor).all()

    # Datos de medicamentos
    medicamentos = [
        {"nombremedicamento": "Paracetamol", "medicamentocontrolado": False, "codigo": "MED001", "cantidad": 50, "lote": "A001", "fecha_vencimiento": date(2025, 5, 10), "precio_unitario": 2.50, "detalle": "Analgésico y antipirético"},
        {"nombremedicamento": "Ibuprofeno", "medicamentocontrolado": False, "codigo": "MED002", "cantidad": 30, "lote": "A002", "fecha_vencimiento": date(2024, 12, 20), "precio_unitario": 3.00, "detalle": "Antiinflamatorio no esteroideo"},
        {"nombremedicamento": "Amoxicilina", "medicamentocontrolado": True, "codigo": "MED003", "cantidad": 20, "lote": "A003", "fecha_vencimiento": date(2025, 8, 15), "precio_unitario": 5.00, "detalle": "Antibiótico de amplio espectro"},
        {"nombremedicamento": "Loratadina", "medicamentocontrolado": False, "codigo": "MED004", "cantidad": 40, "lote": "A004", "fecha_vencimiento": date(2026, 3, 5), "precio_unitario": 4.50, "detalle": "Antihistamínico para alergias"},
        {"nombremedicamento": "Omeprazol", "medicamentocontrolado": False, "codigo": "MED005", "cantidad": 60, "lote": "A005", "fecha_vencimiento": date(2025, 11, 30), "precio_unitario": 6.00, "detalle": "Inhibidor de la bomba de protones"},
        {"nombremedicamento": "Salbutamol", "medicamentocontrolado": True, "codigo": "MED006", "cantidad": 25, "lote": "A006", "fecha_vencimiento": date(2024, 9, 12), "precio_unitario": 7.00, "detalle": "Broncodilatador para asma"},
        {"nombremedicamento": "Metformina", "medicamentocontrolado": False, "codigo": "MED007", "cantidad": 35, "lote": "A007", "fecha_vencimiento": date(2026, 1, 18), "precio_unitario": 3.75, "detalle": "Antidiabético oral"},
        {"nombremedicamento": "Ranitidina", "medicamentocontrolado": False, "codigo": "MED008", "cantidad": 45, "lote": "A008", "fecha_vencimiento": date(2025, 7, 22), "precio_unitario": 4.25, "detalle": "Inhibidor de la secreción gástrica"},
        {"nombremedicamento": "Cefalexina", "medicamentocontrolado": True, "codigo": "MED009", "cantidad": 28, "lote": "A009", "fecha_vencimiento": date(2024, 11, 25), "precio_unitario": 6.50, "detalle": "Antibiótico cefalosporínico"},
        {"nombremedicamento": "Diazepam", "medicamentocontrolado": True, "codigo": "MED010", "cantidad": 15, "lote": "A010", "fecha_vencimiento": date(2026, 2, 14), "precio_unitario": 8.00, "detalle": "Ansiolítico y relajante muscular"},
    ]

    # Insertar medicamentos si no existen
    for data in medicamentos:
        if not session.query(Medicamento).filter_by(codigo=data["codigo"]).first():
            data["proveedor_id"] = random.choice(proveedores).id  # Asignar un proveedor aleatorio
            medicamento = Medicamento(**data)
            session.add(medicamento)

    session.commit()
    session.close()

    print("✅ Datos insertados correctamente.")
