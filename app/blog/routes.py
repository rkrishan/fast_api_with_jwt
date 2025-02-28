# from .import schemas
# from .import models,schemas
# from .database import engine,get_db
# from .hashing import HashPassWord
# from typing import List
# from fastapi import APIRouter,Depends,HTTPException, Response, status
# from sqlalchemy.orm import Session


# router = APIRouter()


# models.Base.metadata.create_all(bind=engine)


# @router.post("/blog/",status_code= status.HTTP_201_CREATED,tags=['blogs'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, content=request.content,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
   
# @router.get("/blog",response_model=list[schemas.ShowBlog],tags=['blogs'])   
# def get_all_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs  


# @router.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog,tags=['blogs'])
# def show(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#     return blog 

# @router.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])   
# def delete_item(id:int,db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id ==id)
#     blog_item = blog.first()
#     if not blog_item:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'No blog with this id: {id} found')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT) 


# @router.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
# def udate_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
#     blog_item = blog.first()
#     if not blog_item:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'No blog with this id: {id} found')

#     update_data = request.dict(exclude_unset=True)

#     blog.update(update_data, synchronize_session=False)
#     db.commit()
#     db.refresh(blog_item)
#     return {"status": "success", "note": blog_item}






# # hashed_password = pwd_context.hash("my_secret_password")
# # print(hashed_password)

# @router.post("/user/",status_code= status.HTTP_201_CREATED,tags=['users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=HashPassWord.hashing(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @router.get("/user/{id}", status_code=200, response_model=schemas.ShowBlog,tags=['users'])
# def show(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#     return blog 


