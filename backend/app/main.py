from enum import Enum

from typing import Optional

from fastapi import FastAPI, Query

from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worlds"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

class Item_model(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items_model/")
async def create_intem(item: Item_model):
    return item

@app.post("/items_model_update/")
async def create_item(item_mod: Item_model):
    item_dict = item_mod.dict()
    if item.tax:
        price_with_tax = item_mode.price + item_mod.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get("/items_ad_val/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results