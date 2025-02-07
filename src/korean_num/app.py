from fastapi import FastAPI
from korean_num.routers import routers

app = FastAPI()
app.include_router(routers)
