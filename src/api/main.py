import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello"}


if __name__ == "__main__":
    os.system("uvicorn src.api.main:app --reload")
