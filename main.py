import uvicorn
from fastapi import FastAPI

from api import api
from db import db_utils
from helpers import env


app = FastAPI(title="Chefster", version="0.0.1")
app.include_router(api.api_router, prefix="/v1")

if __name__ == "__main__":
    args = env.get_arguments()

    db_utils.create_db_and_tables()

    uvicorn.run("main:app", host="0.0.0.0", port=args.port, reload=args.reload)
