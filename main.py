from fastapi import FastAPI
from src.infrastructure.routes import (
    medical_history_routes,
    health_routes)
from src.database.mysql import Base, engine
from dotenv import load_dotenv


load_dotenv()


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(medical_history_routes.router, prefix="/api/v1")
app.include_router(health_routes.router, prefix="/api/v2")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
