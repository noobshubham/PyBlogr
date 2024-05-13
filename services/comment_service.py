from database.models import Comment
from config.config import blogs_collection
from bson import ObjectId

class CommentService:
    async def get_comments_for_post(self, post_id: str):
        comments = await blogs_collection.comments.find({"post_id": post_id}).to_list(None)
        for comment in comments:
            comment["_id"] = str(comment["_id"])
        return comments

    async def create_comment_for_post(self, post_id: str, comment: Comment):
        comment_data = comment.dict()
        comment_data["post_id"] = post_id
        result = await blogs_collection.comments.insert_one(comment_data)
        comment = await blogs_collection.comments.find_one({"_id": result.inserted_id})
        comment["_id"] = str(comment["_id"])
        return comment

    async def update_comment(self, comment_id: str, comment: Comment):
        post_id = await blogs_collection.comments.find_one({"_id": ObjectId(comment_id)})
        comment_dict = comment.dict()
        comment_dict["post_id"] = str(post_id["post_id"])
        await blogs_collection.comments.replace_one({"_id": ObjectId(comment_id)}, comment_dict)
        response_comment = await blogs_collection.comments.find_one({"_id": ObjectId(comment_id)})
        response_comment["_id"] = str(response_comment["_id"])
        return response_comment

    async def delete_comment(self, comment_id: str):
        await blogs_collection.comments.delete_one({"_id": ObjectId(comment_id)})
