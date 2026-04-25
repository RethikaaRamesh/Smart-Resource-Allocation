import React from "react";
import "./App.css";
import TaskForm from "./components/TaskForm";
import AllocationView from "./components/AllocationView";
import Prediction from "./components/Prediction";

function App() {
  return (
    <div className="app">
      <h1>⚡ Smart Resource Allocation</h1>

      <div className="grid">
        <TaskForm />
        <Prediction />
      </div>

      <AllocationView />
    </div>
  );
}

export default App;