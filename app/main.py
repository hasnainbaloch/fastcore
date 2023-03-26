from fastapi import FastAPI, Response, status, HTTPException
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


def find_or_delete_post_by_id(post_id: int, action: str):
    post_dict = {post["id"]: post for post in my_posts}

    if post_id in post_dict:
        post = post_dict[post_id]

        if action == "find":
            return post
        elif action == "delete":
            deletePost(post)
            return {"message": "Post deleted successfully."}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Action {action} is not supported!",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} does not exist!",
        )


@app.get("/posts")
async def get_posts():
    return my_posts


@app.post("/posts")
async def add_post(post: Post, response: Response):
    new_post = post.dict()
    my_posts.append(new_post)
    return new_post


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    post = find_or_delete_post_by_id(post_id, "find")
    return post


@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    post = find_or_delete_post_by_id(post_id, "delete")
    return post
