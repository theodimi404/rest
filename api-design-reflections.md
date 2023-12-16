## Selected Framework

I chose Django, coupled with the Django Rest Framework (DRF), as the core technologies for building this API. 
DRF simplifies the process of building RESTful APIs within the Django ecosystem.


## Coding Standards

All source code files in this project are following the PEP 8 style guide


## Layered Architecture

### Model Layer

The model layer consists of a dedicated model for the `Course` resource.
A custom manager, specifically tailored for the `Course` model, has been introduced. 
This manager encapsulates query-related operations, allowing for a more expressive and organized way to interact with the database. 
By utilizing a custom manager, we centralize query logic and ensure a clean separation of concerns within the model layer.

### Views Layer

The views layer adopts a "thin views" approach. Views are kept lightweight, focusing on handling HTTP requests and responses. 
The majority of the business logic is shifted to a dedicated services layer.

### Services Layer

The services layer acts as an intermediary between the views and models, handling the business logic of the application. 
By centralizing logic in services, we avoid the common pitfall of having "fat models". Each service is designed to encapsulate a specific set of related functionalities, promoting maintainability and code organization.


## Commit Messages

For maintaining a clear and structured commit history, this project follows the Conventional Commits specification for all commit messages.


## API Documentation

To provide comprehensive API documentation, the project utilizes the `drf-yasg` package that integrates with the Django Rest Framework,
giving the ability to create a swagger and a redoc documentation page

## Env Variables

I treated it as a development project, and I didn't include a .env file with secrets (for example the db password).

## Tests

For testing the views methods, I included a file ```tests.py``` in the ```course``` app. You can run them with
```bash
docker exec rest_web_1 python manage.py test course