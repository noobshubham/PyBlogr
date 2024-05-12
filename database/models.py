from pydantic import BaseModel, Field
import uuid

class Post(BaseModel):
    title: str
    content: str
    author: str
    likes: int = 0
    dislikes: int = 0

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            'examples': [
                {
                    "title": "First Post",
                    "content": "This is the content of the first post.",
                    "author": "John Doe",
                    "likes": 1,
                    "dislikes": 2
                }
            ]
        }

class Comment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    text: str
    author: str
    post_id: str

    class Config:
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class Like(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str

    class Config:
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}
