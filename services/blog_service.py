from database.models import Post
from config.config import blogs_collection
from bson import ObjectId

class BlogService:
    async def get_all_posts(self):
        result = []
        for post in await blogs_collection.posts.find().to_list(None):
            post["_id"] = str(post["_id"])
            result.append(post)
        return result
    
    async def get_post_by_id(self, post_id: str):
        return await blogs_collection.posts.find_one({"_id": ObjectId(post_id)})

    async def create_post(self, post: Post):
        response = await blogs_collection.posts.insert_one(post.dict())
        post_dict = await blogs_collection.posts.find_one({"_id": response.inserted_id})
        post_dict["_id"] = str(response.inserted_id)
        return post_dict

    async def update_post(self, post_id: str, post: Post):
        await blogs_collection.posts.replace_one({"_id": ObjectId(post_id)}, post.dict())
        post_dict = await blogs_collection.posts.find_one({"_id": ObjectId(post_id)})
        post_dict["_id"] = str(post_id)
        return post_dict

    async def delete_post(self, post_id: str):
        await blogs_collection.posts.delete_one({"_id": ObjectId(post_id)})
