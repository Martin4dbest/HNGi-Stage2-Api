# API Documentation

## Overview

This API provides endpoints for managing a list of persons. It allows you to create, read, update, and delete persons from the database.


## UML and E-R Diagram

![ULM and E-R Diagram](./public/UML.png)


## Base URL

The base URL for all endpoints is `http://localhost:5000/api`. Replace `localhost` with the appropriate domain if hosted on a server.

## Standard Request and Response Formats

### Create a New Person (POST /api)

**Request Format:**

- HTTP Method: POST
- URL: `/api`
- Request Body: JSON
  - `name` (string, required): The name of the person to be created.

**Response Format:**

- HTTP Status Code: 201 (Created)
- Response Body: JSON
  - `message` (string): Confirmation message.

### Get a Person by ID (GET /api/<int:user_id>)

**Request Format:**

- HTTP Method: GET
- URL: `/api/<int:user_id>`
- Path Parameter:
  - `user_id` (integer, required): The ID of the person to retrieve.

**Response Format:**

- HTTP Status Code: 200 (OK)
- Response Body: JSON
  - `id` (integer): The ID of the person.
  - `name` (string): The name of the person.

### Update a Person by ID (PUT /api/<int:user_id>)

**Request Format:**

- HTTP Method: PUT
- URL: `/api/<int:user_id>`
- Path Parameter:
  - `user_id` (integer, required): The ID of the person to update.
- Request Body: JSON
  - `name` (string, required): The updated name of the person.

**Response Format:**

- HTTP Status Code: 200 (OK)
- Response Body: JSON
  - `message` (string): Confirmation message.

### Delete a Person by ID (DELETE /api/<int:user_id>)

**Request Format:**

- HTTP Method: DELETE
- URL: `/api/<int:user_id>`
- Path Parameter:
  - `user_id` (integer, required): The ID of the person to delete.

**Response Format:**

- HTTP Status Code: 200 (OK)
- Response Body: JSON
  - `message` (string): Confirmation message.

## Sample Usage

### Create a New Person

**Request:**

```http
POST /api
Content-Type: application/json
```


```jason
{
  "name": "John Doe"
}

```


**Response (201 Created):**

```jason
{
  "message": "Person created successfully"
}
```
### Get a Person by ID
**Request:**

```http
GET /api/persons/1

**Response (200 OK):**

```
```jason
{
  "id": 1,
  "name": "John Doe"
}


```

```http
**Response (404 Not Found):**

```
```jason
{
  "error": "Person not found."
}

```


### Update a Person by ID
**Request:**

```http
PUT /api/persons/1
Content-Type: application/json

```

```jason
{
  "name": "Jane Smith"
}

```


**Response (200 OK):**
```jason
{
  "message": "Person updated successfully"
}



```


**Response (404 Not Found):**
```jason
{
  "error": "Person not found."
}


```

### Delete a Person by ID
**Request:**

```http
DELETE /api/persons/1

```


**Response (200 OK):**

```jason
{
  "message": "Person deleted successfully"
}

```
**Response (404 Not Found):** 


```jason
{
  "error": "Person not found."
}

```

## Testing
API endpoints can be tested easily using python script with the requests library to test each CRUD operation:

Create a new person.
Retrieve details of a person.
Update the details of an existing person.
Remove a person.
Retrieve details of a person by name.

Python script to create a person:
````
import requests

url = 'http://localhost:5000/api/person'

data = {
    "name": "Mark Essien",
    "age": 35,
    "email": "mark@example.com"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

```

## Known Limitations and Assumptions
This API assumes a SQLite database named persons.db for storing person records.
Error responses include simple error messages for demonstration purposes.
No authentication or authorization mechanisms are implemented.
Rate limiting is not implemented.


## Setup and Deployment
To set up and run the API locally, follow these steps:

1. Clone the repository:


git clone https://github.com/yourusername/your-repo.git 
cd your-repo

2. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt

4. Run the Flask app:

python app.py
The API will be accessible at http://localhost:5000/api.

5. For deployment on a server, follow your server hosting provider's guidelines for deploying Python Flask applications.
