from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

# Crea una instancia de la clase FastAPI y la asigna a la variable app. Esta instancia será nuestra aplicación web FastAPI principal donde definiremos nuestras rutas y lógica de
#   manejo de solicitudes.
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Esto es un decorador que especifica que la función siguiente manejará las solicitudes GET en la ruta /
# Si o si tenes que pasaarle una ruta al decorador
@app.get("/")
def read_root():
    return {"Funciono": "Mas bien loquita"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}