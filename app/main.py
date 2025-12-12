from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running"}


@app.get("/test")
def root():
    return {"message":"test"}