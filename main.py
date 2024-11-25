from fastapi import FastAPI
from dotenv import load_dotenv
import openai 
import os
from fastapi.staticfiles import StaticFiles
from chat import chat
import contextlib 

@contextlib.asynccontextmanager
async def lifespan(app):
    yield 

app = FastAPI(lifespan=lifespan)


app.mount("/view", StaticFiles(directory="view"), name="static")


app.include_router(chat.router)



