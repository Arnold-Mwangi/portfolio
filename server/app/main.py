from fastapi import FastAPI
from routers import tech


app = FastAPI()

app.include_router(tech.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
