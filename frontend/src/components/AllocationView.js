import React, { useState } from "react";

function AllocationView() {
  const [data, setData] = useState([]);

  const fetchAllocation = async () => {
    const res = await fetch("http://127.0.0.1:5000/allocate");
    const result = await res.json();
    setData(result);
  };

  return (
    <div className="card full">
      <h2>Allocation Results</h2>
      <button onClick={fetchAllocation}>Run Allocation</button>

      {data.map((d, i) => (
        <div key={i} className="result">
          {d.task} → {d.allocated}
        </div>
      ))}
    </div>
  );
}

export default AllocationView;