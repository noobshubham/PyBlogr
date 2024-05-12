from database.models import Post
from config.config import db_connection

class BlogService:
    async def get_all_posts(self):
        return await db_connection.posts.find().to_list(None)

    async def get_post_by_id(self, post_id: str):
        return await db_connection.posts.find_one({"_id": post_id})

    async def create_post(self, post: Post):
        result = await db_connection.posts.insert_one(post.dict())
        return await db_connection.posts.find_one({"_id": result.inserted_id})

    async def update_post(self, post_id: str, post: Post):
        await db_connection.posts.replace_one({"_id": post_id}, post.dict())
        return await db_connection.posts.find_one({"_id": post_id})

    async def delete_post(self, post_id: str):
        await db_connection.posts.delete_one({"_id": post_id})
