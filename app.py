import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return "The PyBlogr API is UP! Maintained and Developed by SHUBHAM."