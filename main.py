from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/blog")
async def index(limit: int = 10, published: bool = True):
    if published:
        return {"data": f"Blog List {limit} {published}"}
    else:
        return {"data": f"Blog List has {limit} unpublished items"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "Unpublished"}


@app.get("/blog/{id}")
async def show(id: int):
    # fetch blog with id = id
    return {"Blog": id}


@app.get("/blog/{id}/comments")
async def comments(id: int, limit: int = 10):
    # fetch comments of blog id = id
    return {"data": ["1", "2"]}


