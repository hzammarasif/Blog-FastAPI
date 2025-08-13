 
from fastapi import Depends ,HTTPException, status
from .token import verifyTheToken 
from . import database, models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")      #url from where the fast api will get the token


def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
     
    email = verifyTheToken(token, credentials_exception)
    user = db.query(models.UsersModel).filter(models.UsersModel.email == email).first()
    if user is None:
        raise credentials_exception
    return user  # return actual User object