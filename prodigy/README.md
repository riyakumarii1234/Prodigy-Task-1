# User Management REST API

This is a simple User Management REST API built with FastAPI. It allows you to create, read, update, and delete users. The API uses an in-memory database (data will be lost when the server restarts) and automatically generates unique user IDs.

## Features
- Create a new user (with automatic UUID id)
- Get all users
- Get a user by id
- Update a user
- Delete a user
- Input validation and error handling
- Interactive API documentation (Swagger UI and ReDoc)

## Requirements
- Python 3.8+

## Setup Instructions
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```
4. **Open your browser and navigate to:**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Create a User
- **POST** `/users`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```
- **Response:**
  ```json
  {
    "id": "<generated-uuid>",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```

### Get All Users
- **GET** `/users`

### Get a User by ID
- **GET** `/users/{user_id}`

### Update a User
- **PUT** `/users/{user_id}`
- **Request Body:** (any fields to update)
  ```json
  {
    "name": "Jane Doe"
  }
  ```

### Delete a User
- **DELETE** `/users/{user_id}`

## Notes
- The database is in-memory; all data will be lost when the server restarts.
- The API validates email format and age.
- Each user must have a unique email address.

## License
This project is for educational/demo purposes. 