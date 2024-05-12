PyBlogr
===========

"PyBlogr" is a Python-based RESTful API project designed to create, manage, and interact with blog posts. It leverages the FastAPI framework for efficient development and stores data in a MongoDB database. Users can perform CRUD operations on blog posts, comment on posts, and like/dislike them, all through a simple and intuitive API interface

For more information, [Documentation](https://pyblogr.onrender.com/docs)


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

[Get your Atlas cluster](https://docs.atlas.mongodb.com/getting-started/) with [sample data](https://docs.atlas.mongodb.com/sample-data/) set [connection string](https://docs.atlas.mongodb.com/connect-to-cluster/) and place in `DB_URI` parameter under `.ini`

Make sure you have IP in the Atlas [access list](https://docs.atlas.mongodb.com/security/add-ip-address-to-list/) and username/password of your Atlas user correctly specified.


Resources
----------

[How to Use Python with MongoDB](https://www.mongodb.com/resources/languages/python)

