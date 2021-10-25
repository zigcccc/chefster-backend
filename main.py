from fastapi import FastAPI

from api import api


app = FastAPI(title="Recipista", version="0.0.1")
app.include_router(api.api_router, prefix="/v1")
