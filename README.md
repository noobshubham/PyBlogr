PyBlogr
===========

"PyBlogr" is a Python-based RESTful API project designed to create, manage, and interact with blog posts. It leverages the FastAPI framework for efficient development and stores data in a MongoDB database. Users can perform CRUD operations on blog posts, comment on posts, and like/dislike them, all through a simple and intuitive API interface

Final Assignment Overview:
You are tasked with building a RESTful API for a simple blogging platform. The API should allow users to create, read, update, and delete blog posts, comment on posts, and like/dislike them. The data should be stored in a MongoDB database. You are required to implement the API using Python FASTAPI framework while adhering to object-oriented programming principles.

Submission Guidelines:
Please submit your codebase along with clear instructions for setting up and running the API locally.
Include any necessary configuration files and dependencies.
Provide documentation detailing the API's usage, data models, and any additional notes or considerations.

Evaluation Criteria:
You will be evaluated based on the correctness and functionality of the implemented API, adherence to RESTful and object-oriented programming principles, code quality and organization, error handling, input validation, and documentation quality and completeness.


Usage
---------

Send a get request to the events endpoint.

Example - https://pyblogr.onrender.com/

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


Resources
----------

[How to Use Python with MongoDB](https://www.mongodb.com/resources/languages/python)

