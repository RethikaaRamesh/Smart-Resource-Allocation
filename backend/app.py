from flask import Flask, request, jsonify
from flask_cors import CORS

from database import init_db, insert_task, fetch_tasks
from scheduler import greedy_allocation
from model import train, predict

app = Flask(__name__)
CORS(app)

init_db()
train()

@app.route("/")
def home():
    return "Smart Resource Allocation API Running"

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.json
    insert_task(data["name"], int(data["priority"]), int(data["demand"]))
    return jsonify({"message": "Task added successfully"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(fetch_tasks())

@app.route("/allocate", methods=["GET"])
def allocate():
    tasks = fetch_tasks()
    result = greedy_allocation(tasks)
    return jsonify(result)

@app.route("/predict", methods=["POST"])
def ml_predict():
    data = request.json
    value = float(data["input"])
    result = predict(value)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)