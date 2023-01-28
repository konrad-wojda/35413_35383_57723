from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routes import router as api_router
import uvicorn

app = FastAPI()


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

templates = Jinja2Templates(directory="templates")

if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='127.0.0.1')
