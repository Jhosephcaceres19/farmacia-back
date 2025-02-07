from fastapi.testclient import TestClient
from app.main import app  # Importamos la app de FastAPI

client = TestClient(app)

def test_read_main():
    response = client.get("/jose")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la base de datos de farmacia"}  # Ajusta según tu respuesta esperada

# Test para obtener un usuario por ID
def test_get_usuario():
    response = client.get("/usuarios/1")  # Ajusta el ID según tus datos de prueba
    assert response.status_code == 200
    assert "nombre" in response.json()
    assert "correoelectronico" in response.json()

# Test para crear un proveedor
def test_create_proveedor():
    nuevo_proveedor = {
        "nombre": "Proveedor Test",
        "telefono": "71234567",
        "direccion": "Calle de prueba #123",
        "correoelectronico": "test_proveedor@example.com"
    }
    response = client.post("/proveedores/", json=nuevo_proveedor)
    assert response.status_code == 200 #para que aya error cambia 201
    assert response.json()["nombre"] == "Proveedor Test"

# Test para obtener la lista de medicamentos
def test_get_medicamentos():
    response = client.get("/medicamentos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica que se devuelva una lista
    if response.json():
        assert "nombremedicamento" in response.json()[0]
