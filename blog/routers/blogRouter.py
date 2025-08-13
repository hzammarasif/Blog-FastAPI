from .. import models
from .. import schemas
from .. import database, oAuth2
from typing import List
from fastapi import FastAPI, Depends,APIRouter, Response, status,HTTPException
from sqlalchemy.orm import Session
from ..repository import blogRepository


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
    )



@router.get('/', response_model= List[schemas.ShowBlog])
def allBlogs(db: Session=Depends(database.get_db),current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.get_all(db=db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogBase,db: Session = Depends(database.get_db),current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.create(db=db, request=request, current_user_id=current_user.id)




@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int,response: Response ,db: Session= Depends(database.get_db),current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.getById(id = id, db=db)




@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session= Depends(database.get_db),current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.destroy(id = id, db=db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int,request: schemas.Blog, db: Session= Depends(database.get_db),current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.edit(id=id, request=request, db= db)
