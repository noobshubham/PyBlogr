PyBlogr
===========

"PyBlogr" is a Python-based RESTful API project designed to create, manage, and interact with blog posts. It leverages the FastAPI framework for efficient development and stores data in a MongoDB database. Users can perform CRUD operations on blog posts, comment on posts, and like/dislike them, all through a simple and intuitive API interface


Usage
---------

Send a get request to the blogs endpoint.

Example - https://pyblogr.onrender.com/docs/posts

For more information, [Documentation](https://pyblogr.onrender.com/docs)

Response Format
-------------------

This is how the JSON Object in response appears. 

```JSON
{
   "title": "Musical Post",
   "content": "Honthon Pe Bas.",
   "author": "Kumar Sanu",
   "likes": 10,
   "dislikes": 2
},
{
   "title": "Musical Post",
   "content": "Tu Hi Meri Sab Hai",
   "author": "KK",
   "likes": 8,
   "dislikes": 2
}
```


Setup
------

Install all dependencies listed in _requirements.txt_ file.

1. To install all dependencies run

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server

   ```bash
   python -m uvicorn app:app --reload
   ```

Rename the `sample_env` to `.env`.

[Get your Atlas cluster](https://docs.atlas.mongodb.com/getting-started/) with [sample data](https://docs.atlas.mongodb.com/sample-data/) set [connection string](https://docs.atlas.mongodb.com/connect-to-cluster/) and place in `DB_URI` parameter under `.env`

Make sure you have IP in the Atlas [access list](https://docs.atlas.mongodb.com/security/add-ip-address-to-list/) and username/password of your Atlas user correctly specified.


Resources
----------

[How to Use Python with MongoDB](https://www.mongodb.com/resources/languages/python)

