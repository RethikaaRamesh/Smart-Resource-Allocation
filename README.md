# ⚡ Smart Resource Allocation Framework

A full-stack intelligent system that optimizes resource allocation using **Machine Learning, OS Scheduling, DBMS, and Greedy Algorithms**.

---

## 🚀 Project Overview

The Smart Resource Allocation Framework is designed to efficiently allocate limited resources among multiple tasks by combining:

- 🤖 Machine Learning (Prediction)
- 🧠 Operating System Scheduling (Priority Scheduling)
- 🗄️ Database Management (SQLite)
- ⚡ Greedy Algorithm (Optimal Allocation)

This system ensures **efficient utilization**, **fair distribution**, and **predictive decision-making**.

---

## 🛠️ Tech Stack

### Frontend
- React.js (Dark Theme UI)
- CSS

### Backend
- Flask (Python)

### Database
- SQLite

### Machine Learning
- Scikit-learn (Linear Regression)

### Tools
- Git & GitHub
- Docker (optional)
- Render (deployment)

---

## 📊 Features

- ✅ Add tasks with priority and demand
- ✅ Predict resource requirements using ML
- ✅ Allocate resources using Greedy Algorithm
- ✅ Priority-based scheduling (OS concept)
- ✅ Dark-themed interactive UI
- ✅ REST API integration

---

## 🧠 Algorithms Used

### 1. Priority Scheduling (OS)
Tasks are executed based on priority (higher first).

### 2. Greedy Algorithm
Allocates maximum available resources step-by-step.

### 3. Machine Learning (Linear Regression)
Predicts resource demand based on input data.

---

## 📁 Project Structure
```
Smart-Resource-Allocation/
│
├── backend/
│ ├── app.py
│ ├── database.py
│ ├── model.py
│ ├── scheduler.py
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│
├── .gitignore
└── README.md

```
---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py

Runs on: http://127.0.0.1:5000

🔹 Frontend Setup
cd frontend
npm install
npm start

Runs on: http://localhost:3000

🔗 API Endpoints
Method	Endpoint	Description
POST	/add_task	Add new task
GET	/allocate	Run allocation
POST	/predict	ML prediction
🧪 Sample Input
Task	 Priority	Demand
AI Job	 10	     60
Web App	  7	     30
Testing	  3  	   50

📈 Expected Output
AI Job → 60
Web App → 30
Testing → 10

🎯 Applications
Cloud Resource Management
Task Scheduling Systems
Data Centers
Distributed Systems
📌 Advantages
Efficient resource utilization
Predictive decision making
Scalable architecture
User-friendly interface
🔮 Future Enhancements
Advanced ML models (Neural Networks)
Real-time analytics dashboard
Cloud auto-scaling integration
Authentication system

👨‍💻 Author

Rethikaa Ramesh

📜 License

This project is for educational purposes.


---

