from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Post(BaseModel):
    title: str
    content: str
    id: int


my_posts = [
    {"id": 1, "title": "First post", "content": "This is my first post"},
    {"id": 2, "title": "Second post", "content": "This is my second post"},
]


def deletePost(post):
    my_posts.remove(post)


def Post_by_id(post_id: int):
    for post in my_posts:
        if post["id"] == post_id:
            deletePost(post)
        else:
            return False


@app.get("/posts")
async def get_posts():
    return my_posts


@app.post("/posts")
async def add_post(post: Post):
    new_post = post.dict()
    my_posts.append(new_post)
    return my_posts[-1]


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    return my_posts[post_id - 1]


@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    if Post_by_id(post_id):
        return {"message": "Post deleted successfully"}
    else:
        return {"error": "Post not found"}
