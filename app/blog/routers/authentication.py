import schemas
import models
import auth_token
from hashing import HashPassWord
from database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter,Depends,HTTPException,status
from datetime import datetime, timedelta, timezone
router = APIRouter(

    tags=["Authentication"]
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()    

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not HashPassWord.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    
    access_token = auth_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    
   
