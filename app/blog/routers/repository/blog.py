import models
import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs  

def get_blog_as_per_id(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog 

def create(request: schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title, content=request.content,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    blog_item = blog.first()
    if not blog_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No blog with this id: {id} found')
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

def update(id:int,request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    blog_item = blog.first()
    if not blog_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No blog with this id: {id} found')

    update_data = request.dict(exclude_unset=True)

    blog.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(blog_item)
    return {"status": "success", "note": blog_item}


