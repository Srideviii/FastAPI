import uvicorn
from fastapi import FastAPI
from scripts.core.services.book_service import app
app_main = FastAPI()

app_main.include_router(app)

if __name__ == "main__":
    uvicorn.run("main:app_main")
