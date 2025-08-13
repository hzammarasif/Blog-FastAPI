from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import FastAPI, Depends,APIRouter, Response, status,HTTPException
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto")


def creatingUser(db: Session, request: schemas.BlogBase):
    hashedPassword = pwd_cxt.hash(request.password)
    user = models.UsersModel(name = request.name, email = request.email, password = hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def getUserById(db: Session, id: int):
    user = db.query(models.UsersModel).filter(models.UsersModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user with the id {id} was not found")
    return user    