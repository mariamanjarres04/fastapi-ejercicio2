from fastapi import FastAPI

app = FastAPI()
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str
    quantity: int

productos = [
    {
        "id": 1,
        "nombre": "Teclado mecánico",
        "precio": 180000,
        "categoria": "electrónica",
        "quantity": 10
    },
    {
        "id": 2,
        "nombre": "Mouse inalámbrico",
        "precio": 85000,
        "categoria": "electrónica",
        "quantity": 15
    },
    {
        "id": 3,
        "nombre": "Silla ergonómica",
        "precio": 650000,
        "categoria": "muebles",
        "quantity": 5
    },
    {
        "id": 4,
        "nombre": "Teclado inalámbrico",
        "precio": 120000,
        "categoria": "electrónica",
        "quantity": 8
    },
    {
            "id": 5,
            "nombre": "Memoria usb",
            "precio": 47000,
            "categoria": "electrónica",
            "quantity": 8
        }

]

@app.get("/productos")
def obtener_productos():
    return productos