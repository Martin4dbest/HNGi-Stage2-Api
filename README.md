# RESTful Person API

A This is a simple RESTful API for managing person records.

## Table of Contents

- [Endpoints](#endpoints)
  - [Get a Person by ID](#get-a-person-by-id)
  - [Update a Person by ID](#update-a-person-by-id)
  - [Delete a Person by ID](#delete-a-person-by-id)
- [Testing] (#Testing)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)
- [Local Setup and Deployment](#local-setup-and-deployment)

## Endpoints

### Get a Person by ID

**Request:**

```http
GET /api/1

```jason
{
  "id": 1,
  "name": "John Doe"
}

```

### Update a Person by ID
**Request:**

```http

PUT /api/1
Content-Type: application/json

```jason
{
  "name": "Jane Smith"
}  
```
**Response (200 OK):**

```json
{
  "message": "Person updated successfully"
}
```

### Delete a Person by ID
**Request:**

```http

DELETE /api/1
**Response (200 OK):**
```

```json
Copy code
{
  "message": "Person deleted successfully"
}
```

