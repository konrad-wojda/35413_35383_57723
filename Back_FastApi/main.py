from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routes import router as api_router
import uvicorn


app = FastAPI()


@app.get("/health_check")
async def health_check():
    """
    Checks if server is working
    :return: simple message that server is running
    """
    return "Server is running"


@app.get("/", include_in_schema=False)
async def health_check():
    """
    Checks if server is working
    :return: simple message that server is running
    """
    return RedirectResponse(url='/docs')

origins = [
    # "http://localhost",
    # "http://localhost:4200"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(app, port=80, host='127.0.0.1')
