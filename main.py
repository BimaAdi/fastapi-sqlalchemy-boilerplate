from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.health_check import health_check
from core.log import logger

health_check()


app = FastAPI(title="PyconId Boilerplate!")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    logger.info("hello")
    return {"Hello": "from pyconid boilerplate!"}
