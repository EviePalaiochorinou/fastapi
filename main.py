from urllib.request import Request
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import blog_get, blog_post, user, article
from auth import authentication
from db import models
from db.database import engine
from router.exceptions import StoryException
from fastapi import HTTPException, status
from starlette.responses import PlainTextResponse

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(authentication.router)

@app.get('/')
def index():
    return {"message": "For the API, please go to /docs"}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code = 418,
        content = {'detail': exc.name}
    )

models.Base.metadata.create_all(engine)
