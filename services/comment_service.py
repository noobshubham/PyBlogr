from database.models import Comment
from config.config import db_connection

class CommentService:
    async def get_comments_for_post(self, post_id: str):
        return await db_connection.comments.find({"post_id": post_id}).to_list(None)

    async def create_comment_for_post(self, post_id: str, comment: Comment):
        comment_data = comment.dict()
        comment_data["post_id"] = post_id
        result = await db_connection.comments.insert_one(comment_data)
        return await db_connection.comments.find_one({"_id": result.inserted_id})

    async def update_comment(self, comment_id: str, comment: Comment):
        await db_connection.comments.replace_one({"_id": comment_id}, comment.dict())
        return await db_connection.comments.find_one({"_id": comment_id})

    async def delete_comment(self, comment_id: str):
        await db_connection.comments.delete_one({"_id": comment_id})
