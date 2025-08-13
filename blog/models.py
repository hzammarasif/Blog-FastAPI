from sqlalchemy.orm import Mapped, mapped_column
from .database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)
    user_Id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    creator = relationship("UsersModel", back_populates="blogs")

class UsersModel(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str]= mapped_column(String)
    password: Mapped[str]= mapped_column(String)
    email: Mapped[str]= mapped_column(String)

    blogs = relationship('Blog', back_populates="creator")