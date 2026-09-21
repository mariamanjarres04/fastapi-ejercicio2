from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Molde de cada producto
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str
    quantity: int

# Productos guardados en memoria
productos = [
    {"id": 1, "nombre": "Teclado mecánico", "precio": 180000, "categoria": "electrónica", "quantity": 10},
    {"id": 2, "nombre": "Mouse inalámbrico", "precio": 85000, "categoria": "electrónica", "quantity": 15},
    {"id": 3, "nombre": "Silla ergonómica", "precio": 650000, "categoria": "muebles", "quantity": 5},
    {"id": 4, "nombre": "Teclado inalámbrico", "precio": 120000, "categoria": "electrónica", "quantity": 8},
    {"id": 5, "nombre": "Memoria usb", "precio": 47000, "categoria": "electrónica", "quantity": 8},
]

# Lista los productos
@app.get("/productos")
def obtener_productos():
    return productos

# Busca un producto por su id
@app.get("/productos/{id}")
def obtener_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return producto
    raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
