from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blogRouter, userRouter, authentacation
app = FastAPI()


models.Base.metadata.create_all(bind = engine)

app.include_router(blogRouter.router)
app.include_router(userRouter.router)
app.include_router(authentacation.router)



