import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes.offramp import router as offramp_router
from app.services.offramp_client import offramp_client
from app.logger import logger

@asynccontextmanager
async def lifespan(api: FastAPI):
    """
    Handles startup and shutdown events.
    - On startup: The offramp_client is attached to the app state.
    - On shutdown: The offramp_client's session is closed gracefully.
    """
    logger.info("Starting Universal Offramp service...")
    api.state.offramp_client = offramp_client
    yield
    logger.info("Shutting down Universal Offramp service...")
    await api.state.offramp_client.close()

# Create the FastAPI application instance
app = FastAPI(
    title="Universal Offramp Rail API",
    description="A structured FastAPI wrapper for the Bread.africa API.",
    version="3.0.0", # Incremented version
    lifespan=lifespan
)

# Include the router from the offramp routes file
app.include_router(offramp_router)

@app.get("/", tags=["Health"])
async def root():
    """A simple health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Universal Offramp Rail API!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)