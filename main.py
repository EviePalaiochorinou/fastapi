from lib2to3.pgen2.token import OP
from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello world!"}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All blogs"}

@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int]=None):
    return {"message": f"All {page_size} blogs on page {page}"}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str]=None):
    return {"message": f"blog id {id}, comment id {comment_id}, valid {valid}, username {username}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}

@app.get('/blog/{id}')
def index(id: int):
    return {"message": f"Blog with id {id}"}