from fastapi import FastAPI

from blog.schemas import Blog

app = FastAPI()


@app.post("/blog")
async def create_blog(blog: Blog):
    return {"data": f"Blog is created with title {blog.title}, body {blog.body}"}
