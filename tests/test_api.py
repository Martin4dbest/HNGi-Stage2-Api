import requests

# Define the API base URL
base_url = 'http://localhost:5000/api/person'

# Example: Create a new person
data = {
    "name": "Mark Essien",
    "age": 35,
    "email": "mark@example.com"
}

response = requests.post(base_url, json=data)
print("Create a new person:")
print(response.status_code)
print(response.json())

# Example: Retrieve details of a person by ID
user_id = 1
response = requests.get(f'{base_url}/{user_id}')
print("\nRetrieve details of a person by ID:")
print(response.status_code)
print(response.json())

# Example: Update the details of an existing person by ID
user_id = 1
data = {
    "name": "Updated Name",
    "age": 40
}

response = requests.put(f'{base_url}/{user_id}', json=data)
print("\nUpdate the details of an existing person by ID:")
print(response.status_code)
print(response.json())

# Example: Remove a person by ID
user_id = 1
response = requests.delete(f'{base_url}/{user_id}')
print("\nRemove a person by ID:")
print(response.status_code)
print(response.json())
