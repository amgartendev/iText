from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all_models

    print("Initializing database structure...")
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Database setup complete! All tables created successfully.")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
