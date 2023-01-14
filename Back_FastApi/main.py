from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import uvicorn
from routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Terminal: uvicorn main:app --reload --port=7000


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


# @app.get("")
# def read_root(request: Request):
#     return templates.TemplateResponse("main.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='127.0.0.1')
