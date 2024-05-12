from fastapi import FastAPI
from routers import blog, comment, like

app = FastAPI()

@app.get('/')
async def home():
    return "The PyBlogr API is UP! Maintained and Developed by SHUBHAM."

# Include routers
app.include_router(blog.router)
app.include_router(comment.router)
app.include_router(like.router)