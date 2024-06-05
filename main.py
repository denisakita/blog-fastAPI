from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"data": "Blog List"}


@app.get("/blog/unpublished")
async def unpublished():
    return {"data": "Unpublished"}


@app.get("/blog/{id}")
async def show(id: int):
    # fetch blog with id = id
    return {"Blog": id}


@app.get("/blog/{id}/comments")
async def comments(id: int):
    # fetch comments of blog id = id
    return {"data": {"1", "2"}}
