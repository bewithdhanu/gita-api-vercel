from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .routes import router as GitaAPIRouter

app = FastAPI()


@app.get("/", tags = ["Root"], response_class = HTMLResponse)
async def read_root() -> str:
    return "Hi, I'm a GitaTeluguAPI running and powered by vercel."


app.include_router(GitaAPIRouter)
