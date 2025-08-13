
from fastapi import Depends, APIRouter
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import userRepository


router = APIRouter(tags=['Users'])




@router.post('/user', response_model=schemas.ShowUser)
def createUser(request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.creatingUser(request=request, db=db)



@router.get('/user/{id}', response_model=schemas.ShowUser)
def getUSerByID(id, db: Session = Depends(get_db)):
    return userRepository.getUserById(db=db, id=id)        
         
