import React, { useState } from "react";

function Prediction() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({input})
    });

    const data = await res.json();
    setResult(data.prediction);
  };

  return (
    <div className="card">
      <h2>ML Prediction</h2>
      <input placeholder="Enter value"
        onChange={(e)=>setInput(e.target.value)} />
      <button onClick={predict}>Predict</button>

      {result && <p>Prediction: {result}</p>}
    </div>
  );
}

export default Prediction;