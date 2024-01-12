from fastapi import FastAPI
from .routes.user import router
from .routes.product import router2
from .routes.order import router3
from .routes.order_product import router4

app = FastAPI(
    title="My Awesome API",
    description="API description goes here",
    version="1.0.0"
)

app.include_router(router)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)
