from pydantic import BaseModel, Field
import uuid
from bson import ObjectId

class Post(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    content: str
    author: str
    likes: int = 0
    dislikes: int = 0

    class Config:
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

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
