from fastapi import FastAPI
from routs import base
from routs import data


app  = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)