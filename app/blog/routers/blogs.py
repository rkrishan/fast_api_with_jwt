import schemas
import models
import oauth2
from database import engine, get_db
from typing import List
from sqlalchemy.orm import Session
from .repository  import blog
from fastapi import APIRouter,Depends, status


router = APIRouter(

    prefix="/blogs",
    tags=["blogs"]
)

@router.post("/",status_code= status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request,db)


@router.get("/",response_model=list[schemas.ShowBlog])   
def all(db: Session = Depends(get_db),current_user= Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db),current_user= Depends(oauth2.get_current_user)):
    return blog.get_blog_as_per_id(id,db)
    


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)   
def delete_item(id:int,db: Session = Depends(get_db),current_user= Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def udate_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db),current_user= Depends(oauth2.get_current_user)):
    blog.update(id,request,db)



