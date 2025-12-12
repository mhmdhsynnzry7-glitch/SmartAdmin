from fastapi import FastAPI
from app.model.itemModle import Item
app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running"}


@app.get("/test")
def root():
    return {"message":"test"}


@app.post("/items")
def create_item(item: Item):
    return {
        "status": "created",
        "item": item
    }
