
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import FastAPI, Depends,APIRouter, Response, status,HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs



def create(db: Session, request: schemas.BlogBase, current_user_id: int):
    new_blog = models.Blog(title=request.title, body= request.body, user_Id = current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    

def getById(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with the {id} is not found")
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return f"The blog with the {id} is not found"
    return blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The item with the {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deleted"


def edit(id: int, db: Session, request: schemas.BlogBase):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The item with the {id} is not found")
    
    blog.update(request.dict())
    db.commit()
    return {"message": "Update is successful"}