from database.models import Post
from config.config import db_connection

class LikeService:
    async def like_post(self, post_id: str):
        await db_connection.posts.update_one({"_id": post_id}, {"$inc": {"likes": 1}})
        return {"message": "Post liked successfully"}

    async def dislike_post(self, post_id: str):
        await db_connection.posts.update_one({"_id": post_id}, {"$inc": {"dislikes": 1}})
        return {"message": "Post disliked successfully"}
