from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import SessionLocal, engine
from blog.models import Blog as BlogModel
from blog.schemas import Blog as BlogSchema

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", response_model=BlogSchema)
async def create_blog(request: BlogSchema, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
