import fastapi
from app.api.controller import health
from app.api.controller.v1 import product

app = fastapi.FastAPI()
app.include_router(health.router)
app.include_router(product.router)
