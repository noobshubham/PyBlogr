from database.models import Post
from config.config import blogs_collection
from bson import ObjectId

class BlogService:
    async def get_all_posts(self):
        return await blogs_collection.posts.find().to_list(None)

    async def get_post_by_id(self, post_id: str):
        return await blogs_collection.posts.find_one({"_id": ObjectId(post_id)})

    async def create_post(self, post: Post):
        result = await blogs_collection.posts.insert_one(post.dict())
        return await blogs_collection.posts.find_one({"_id": result.inserted_id})

    async def update_post(self, post_id: str, post: Post):
        await blogs_collection.posts.replace_one({"_id": ObjectId(post_id)}, post.dict())
        return await blogs_collection.posts.find_one({"_id": ObjectId(post_id)})

    async def delete_post(self, post_id: str):
        await blogs_collection.posts.delete_one({"_id": ObjectId(post_id)})
