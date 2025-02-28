import models
import schemas
from sqlalchemy.orm import Session
from hashing import HashPassWord
from fastapi import HTTPException,status


def create_user(request: schemas.User,db:Session):
    new_user = models.User(name=request.name, email=request.email, password=HashPassWord.hashing(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
