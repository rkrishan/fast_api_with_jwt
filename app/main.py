from fastapi import FastAPI
from routers import blogs, users,authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)



