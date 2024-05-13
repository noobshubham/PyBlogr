from fastapi import APIRouter, HTTPException
from typing import List
from database.models import Post
from services.blog_service import BlogService

router = APIRouter()
blog_service = BlogService()

@router.get("/posts", response_model=List)
async def get_all_posts():
    return await blog_service.get_all_posts()

@router.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str):
    post = await blog_service.get_post_by_id(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts", response_model=None)
async def create_post(post: Post):
    return await blog_service.create_post(post)

@router.put("/posts/{post_id}", response_model=None)
async def update_post(post_id: str, post: Post):
    return await blog_service.update_post(post_id, post)

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    await blog_service.delete_post(post_id)
    return {"message": "Post deleted successfully"}
