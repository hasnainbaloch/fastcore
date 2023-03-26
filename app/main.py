from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


myPosts = [
    {"author": "John", "content": "Hello World", "date": "2020-01-01"},
    {"author": "Jane", "content": "Hello World", "date": "2020-01-01"},
]


@app.get("/posts")
async def get_posts():
    return myPosts
