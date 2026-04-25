import React, { useState } from "react";

function TaskForm() {
  const [task, setTask] = useState({
    name: "",
    priority: "",
    demand: ""
  });

  const submit = async () => {
    await fetch("http://127.0.0.1:5000/add_task", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(task)
    });
    alert("Task Added!");
  };

  return (
    <div className="card">
      <h2>Add Task</h2>
      <input placeholder="Task Name"
        onChange={(e)=>setTask({...task,name:e.target.value})}/>
      <input placeholder="Priority"
        onChange={(e)=>setTask({...task,priority:e.target.value})}/>
      <input placeholder="Demand"
        onChange={(e)=>setTask({...task,demand:e.target.value})}/>
      <button onClick={submit}>Add</button>
    </div>
  );
}

export default TaskForm;