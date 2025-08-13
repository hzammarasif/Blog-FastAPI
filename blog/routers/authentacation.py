from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..repository import userRepository




router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session =Depends(database.get_db)):
    user = db.query(models.UsersModel).filter(models.UsersModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Credentials are invalid")
    
    if not userRepository.pwd_cxt.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    
    # generate jwt token and return it

    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
    