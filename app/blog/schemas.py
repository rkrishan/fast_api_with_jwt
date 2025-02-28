from pydantic import BaseModel
from typing import Optional,List

class BlogBase(BaseModel):
    title: str
    content: str

class Blog(BlogBase):
    class Config:
        from_attributes = True


class User(BaseModel):
    name : str
    password : str
    email : str

class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = []

    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title :str
    content : str
    creator : ShowUser
    
    class Config:
        from_attributes = True

class Login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
