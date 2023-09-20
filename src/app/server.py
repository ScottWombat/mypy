import os
from dotenv import load_dotenv
from typing import List

from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api.home.home import home_router
from core.config import config
from core.exceptions import CustomException
from core.fastapi.dependencies import Logging

load_dotenv()

def init_routers(app_: FastAPI) -> None:
    app_.include_router(home_router)

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Mypy",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    
    return app_


app = create_app()