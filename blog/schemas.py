
from pydantic import BaseModel
from typing import List
from typing import Optional






class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config():
        orm_mode = True 


class User(BaseModel):
    name: str
    email:str
    password: str
    

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    class Config():
        orm_mode = True 



class showCreator(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True 

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[showCreator]
    class Config():
        orm_mode = True 



class Login(BaseModel):
    userName:str
    password:str





class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None