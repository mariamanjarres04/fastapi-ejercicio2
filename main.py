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