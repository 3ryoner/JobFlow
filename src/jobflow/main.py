from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from jobflow.api.v1.health import router as health_router
from jobflow.core.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await engine.dispose()


app = FastAPI(
    title="JobFlow API",
    version="0.1.0",
    description="Backend service for JobFlow",
    lifespan=lifespan,
)

app.include_router(health_router)
