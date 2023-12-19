from fastapi import FastAPI
from .routes.user import router

app = FastAPI(
    title="My Awesome API",
    description="API description goes here",
    version="1.0.0"
)

app.include_router(router)
