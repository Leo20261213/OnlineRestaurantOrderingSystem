from fastapi import FastAPI
from api.routers.index import router as api_router

app = FastAPI(title="Online Restaurant Ordering System")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Online Restaurant Ordering System API"}

app.include_router(api_router)