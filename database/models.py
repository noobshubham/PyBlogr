from pydantic import BaseModel

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
    text: str
    author: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            'examples': [
                {
                    "text": "Your Comment!",
                    "author": "Name of the Commentator"
                }
            ]
        }

