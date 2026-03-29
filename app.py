#1. import Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build API", "completed": False}
]

@app.route("/")
def home():
    #just prints hello from flask!
    return "Hello from Flask!"

@app.route("/tasks")
def get_tasks():
    #returns all tasks
    return jsonify(tasks)

@app.route("/tasks/<int:id>")
def get_specific_task(id):
    #Search through tasks
    for task in tasks:
        if task["id"] == id: #if task found, return
            return jsonify(task)
    return jsonify({"error": "Task not found"}) #else, exits loop and displays not found

@app.route("/tasks", methods=["POST"])
def create_task():
    #get JSON data from request
    data = request.get_json()
    # 1. check if JSON exists
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    # 2. check if title exists
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    # 3. check if title is a string
    if not isinstance(data["title"], str):
        return jsonify({"error": "Title must be a string"}), 400
    # 4. check if title is not empty
    if not data["title"].strip():
        return jsonify({"error": "Title cannot be empty"}), 400
    # create a new task dictionary
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }
    # append it to tasks
    tasks.append(new_task)
    # return the new task
    return jsonify(new_task)

@app.route("/tasks/<int:id>", methods=["PUT"])
def put_task(id):
    #Obtaining the Put
    data = request.get_json()
    #User input validation
    if "title" in data:
        if not isinstance(data["title"], str):
            return jsonify({"error": "Title must be a string"}), 400
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify({"error": "Completed must be a boolean"}), 400
    #looping search then update
    for task in tasks:
        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed", task["completed"])
            #returns updated task
            return jsonify(task)
    return jsonify({"error": "Task not found"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    #locate task
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"})

if __name__ == "__main__":
    app.run(debug=True)