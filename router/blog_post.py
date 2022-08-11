from lib2to3.pgen2.token import OP
from re import S
from typing import Optional, List
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=["blog"]
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    num_comments: int
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel,
    id: int, 
    comment_title: int = Query(None,
        title = "Comment title",
        description = "Some kind of description",
        alias = "commentId",
        deprecated = True
        ),
    content: str = Body(..., min_length = 10),
    v: Optional[List[str]] = Query(None),
    comment_id: int = Path(None, gt=5, lt=10)
    ):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id
    }