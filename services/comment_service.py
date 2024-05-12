from database.models import Comment
from config.config import blogs_collection

class CommentService:
    async def get_comments_for_post(self, post_id: str):
        return await blogs_collection.comments.find({"post_id": post_id}).to_list(None)

    async def create_comment_for_post(self, post_id: str, comment: Comment):
        comment_data = comment.dict()
        comment_data["post_id"] = post_id
        result = await blogs_collection.comments.insert_one(comment_data)
        return await blogs_collection.comments.find_one({"_id": result.inserted_id})

    async def update_comment(self, comment_id: str, comment: Comment):
        await blogs_collection.comments.replace_one({"_id": comment_id}, comment.model_dump)
        return await blogs_collection.comments.find_one({"_id": comment_id})

    async def delete_comment(self, comment_id: str):
        await blogs_collection.comments.delete_one({"_id": comment_id})
