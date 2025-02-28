import schemas
import models
from database import engine, get_db
from fastapi import APIRouter,Depends, status
from sqlalchemy.orm import Session
from .repository import user


router = APIRouter(
     prefix="/user",
     tags=["user"]
)



@router.post("/",status_code= status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)
    

@router.get("/{id}", status_code=200, response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.get_user(id,db)


