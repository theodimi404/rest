# Course API

The Course API is a RESTful API designed to manage course resources. It provides a set of endpoints to perform actions related to courses. This project includes a Swagger page and ReDoc for easy API documentation and exploration. Additionally, it is Dockerized for easy installation and deployment.

## API Endpoints

1. **Get All Courses**
   - **Endpoint**: `/courses`
   - **Method**: `GET`
   - Retrieve a list of all available courses.

2. **Create a New Course**
   - **Endpoint**: `/courses`
   - **Method**: `POST`
   - Add a new course to the system.

3. **Get Course by ID**
   - **Endpoint**: `/courses/{courseId}`
   - **Method**: `GET`
   - Retrieve details of a specific course by its ID.

4. **Update Course**
   - **Endpoint**: `/courses/{courseId}`
   - **Method**: `PUT`
   - Update details of a specific course by its ID.

5. **Delete Course**
   - **Endpoint**: `/courses/{courseId}`
   - **Method**: `DELETE`
   - Delete a specific course by its ID.

## API Documentation

Explore and understand the API using the following documentation tools:

- localhost:8000/swagger
- localhost:8000/redoc

## Installation

### Prerequisites

- Docker installed on your machine.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/theodimi404/rest.git
   
2. **Start the Docker containers:**

   ```bash
   docker-compose -f docker-compose.yml up -d
   
3. **Run the migrations:**

   ```bash
   docker exec rest_web_1 python manage.py migrate
   
4. **Access the Django server in:**

   ```bash
   localhost:8000