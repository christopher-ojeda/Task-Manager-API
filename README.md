# Task Manager API

This is a RESTful API built using Flask that allows users to manage tasks. The application supports basic CRUD operations, meaning users can create, read, update, and delete tasks.

This project demonstrates backend development concepts such as handling HTTP requests, working with JSON data, validating user input, and designing API endpoints.

---

## Features

* Retrieve all tasks
* Retrieve a specific task by ID
* Create new tasks
* Update existing tasks
* Delete tasks
* Input validation and error handling

---

## Tech Stack

* Python
* Flask
* JSON

---

## How to Run Locally

1. Clone the repository:

```
git clone https://github.com/Christopher-ojeda/Task-Manager-API.git
cd Task-Manager-API
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

4. Open in browser or API client:

```
http://127.0.0.1:5000/
```

---

## API Endpoints

### Get all tasks

GET /tasks

### Get a specific task

GET /tasks/<id>

### Create a task

POST /tasks

Example request body:

```
{
  "title": "Learn Flask"
}
```

### Update a task

PUT /tasks/<id>

Example request body:

```
{
  "title": "Updated Task",
  "completed": true
}
```

### Delete a task

DELETE /tasks/<id>

---

## Example Response

```
{
  "id": 1,
  "title": "Learn Flask",
  "completed": false
}
```

---

## Error Handling

* 400 Bad Request → Invalid input
* 404 Not Found → Task does not exist

---

## What I Learned

* How to build RESTful APIs using Flask
* How to handle HTTP methods (GET, POST, PUT, DELETE)
* How to validate user input
* How backend systems process and return data

---

## Future Improvements

* Add a database (SQLite or PostgreSQL)
* Add authentication (user login system)
* Deploy the API online

---

## Author

Christopher Ojeda
Florida International University — B.A. Computer Science
