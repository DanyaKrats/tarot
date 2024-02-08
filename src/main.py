from fastapi import FastAPI
from .api import router

def get_application(test: bool = False) -> FastAPI:
    application = FastAPI()
    application.include_router(router)

    return application

app = get_application()