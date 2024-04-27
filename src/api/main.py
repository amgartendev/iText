import env
from database import Base, engine
from fastapi import FastAPI
from users.router import router as users_router

if env.DB_REBUILD:
    Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)
if env.DB_TEST_VALUES:
    import tweaks

    tweaks.listen_for_events()

docs_url = "/docs" if env.DEVELOPER_MODE else None
redoc_url = "/redoc" if env.DEVELOPER_MODE else None

app = FastAPI(docs_url=docs_url, redoc_url=redoc_url)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(users_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, reload=True)
