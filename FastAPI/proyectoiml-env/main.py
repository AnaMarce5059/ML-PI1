from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola, mi nombre es Analía, y este es mi PIMLOps"}

