```markdown
# FastAPI CRUD Blog with User Authentication

This repository demonstrates how to create a full API for a blog with user authentication using FastAPI, Pydantic, and
SQLAlchemy. FastAPI is a high-performance web framework for building APIs with Python 3.12 based on standard Python type
hints.

## Features

- Comprehensive API documentation with Swagger
- User authentication with JWT tokens
- CRUD operations for blogs
- Database integration with SQLAlchemy
- Modern Python type hints for data validation

## Technologies Used

- **FastAPI**: Web framework for building APIs
- **Pydantic**: Data validation and settings management using Python type annotations
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python
- **Starlette**: Lightweight ASGI framework/toolkit, which FastAPI is based on
- **Swagger**: API documentation and testing tool

 ```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/blogFastAPI.git
   cd fastapi-crud-blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation powered by
   Swagger.

## Project Structure

- `main.py`: The entry point of the application.
- `schemas.py`: Pydantic models for request and response validation.
- `models.py`: SQLAlchemy models for the database tables.
- `database.py`: Database configuration and connection.
- `auth.py`: User authentication and JWT token management.
- `routers/`: Directory containing the API routes for blog and user operations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

```
