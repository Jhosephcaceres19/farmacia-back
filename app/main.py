from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import detalle_factura, factura, medicamento, proveedor, usuario
from app.seed import seed_data

# Configurar CORS
app = FastAPI()

# Permitir solicitudes desde el puerto 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes solo desde Next.js
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)

# Ejecutar la carga de datos inicial
seed_data()

@app.get("/jose")
def read_root():
    return {"message": "Bienvenido a la base de datos de farmacia"}

app.include_router(detalle_factura.router, prefix="/detalle_factura", tags=["detalle_factura"])
app.include_router(factura.router, prefix="/factura", tags=["factura"])
app.include_router(medicamento.router, prefix="/medicamentos", tags=["medicamentos"])
app.include_router(proveedor.router, prefix="/proveedores", tags=["proveedores"])
app.include_router(usuario.router, prefix="/usuarios", tags=["usuarios"])

if __name__ == '__main__':
    print("Iniciando el servidor Uvicorn...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=7000)
