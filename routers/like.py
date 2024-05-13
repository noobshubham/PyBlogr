from fastapi import APIRouter
from services.like_service import LikeService

router = APIRouter()
like_service = LikeService()

@router.post("/posts/{post_id}/like")
async def like_post(post_id: str):
    return await like_service.like_post(post_id)

@router.post("/posts/{post_id}/dislike")
async def dislike_post(post_id: str):
    return await like_service.dislike_post(post_id)
