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

# Lista, filtra y pagina los productos
@app.get("/productos")
def obtener_productos(
    skip: int = 0,
    limit: int = 10,
    categoria: str | None = None,
    busqueda: str | None = None
):
    resultado = productos

    if categoria:
        resultado = [
            producto for producto in resultado
            if producto["categoria"].lower() == categoria.lower()
        ]

    if busqueda:
        resultado = [
            producto for producto in resultado
            if busqueda.lower() in producto["nombre"].lower()
        ]

    return resultado[skip:skip + limit]

# Busca un producto por su id
@app.get("/productos/{id}")
def obtener_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return producto
    raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")

# Crea un producto nuevo
@app.post("/productos")
def crear_producto(producto: Producto):
    for item in productos:
        if item["id"] == producto.id:
            raise HTTPException(status_code=400, detail="El id ya existe")

    nuevo_producto = producto.model_dump()
    productos.append(nuevo_producto)
    return nuevo_producto

# Actualiza un producto
@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    for indice, item in enumerate(productos):
        if item["id"] == id:
            datos = producto.model_dump()
            datos["id"] = id
            productos[indice] = datos
            return datos

    raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")

# Elimina un producto
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    for indice, producto in enumerate(productos):
        if producto["id"] == id:
            eliminado = productos.pop(indice)
            return eliminado

    raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
