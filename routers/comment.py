from fastapi import APIRouter
from typing import List
from database.models import Comment
from services.comment_service import CommentService

router = APIRouter()
comment_service = CommentService()

@router.get("/posts/{post_id}/comments", response_model=List)
async def get_comments_for_post(post_id: str):
    return await comment_service.get_comments_for_post(post_id)

@router.post("/posts/{post_id}/comments", response_model=None)
async def create_comment_for_post(post_id: str, comment: Comment):
    return await comment_service.create_comment_for_post(post_id, comment)

@router.put("/comments/{comment_id}", response_model=None)
async def update_comment(comment_id: str, comment: Comment):
    return await comment_service.update_comment(comment_id, comment)

@router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: str):
    await comment_service.delete_comment(comment_id)
    return {"message": "Comment deleted successfully"}
