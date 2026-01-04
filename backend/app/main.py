from fastapi import FastAPI
from app.routes.health import router as health_router
from app.middleware.cors import setup_cors
from app.core.logging import setup_logging

def create_app():
    app = FastAPI(
        title="AION ∞ API",
        version="1.0.0",
        docs_url="/docs"
    )

    setup_logging()
    setup_cors(app)

    app.include_router(health_router, prefix="/health")

    return app

app = create_app()
