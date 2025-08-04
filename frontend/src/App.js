import React, { useState, useEffect } from 'react';

function App() {
  const [status, setStatus] = useState(null);
  const host = "8.8.8.8"; // example: Google DNS

  useEffect(() => {
    fetch(`/api/status/${host}`)
      .then(res => res.json())
      .then(data => setStatus(data));
  }, []);

  return (
    <div className="p-4">
      <h1>Network Status</h1>
      {status ? (
        <div>
          <p>Host: {status.host}</p>
          <p>Reachable: {status.reachable ? "Yes" : "No"}</p>
          <p>Latency: {status.latency} ms</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
