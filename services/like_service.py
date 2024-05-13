from config.config import blogs_collection
from bson import ObjectId

class LikeService:
    async def like_post(self, post_id: str):
        await blogs_collection.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes": 1}})
        return {"message": "Post liked successfully"}

    async def dislike_post(self, post_id: str):
        await blogs_collection.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"dislikes": 1}})
        return {"message": "Post disliked successfully"}
