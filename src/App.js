import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first!");
      return;
    }
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult(response.data.vad_results);
    } catch (error) {
      console.error('Error uploading file:', error);
      alert("Error uploading file.");
    }
  };

  return (
    <div className="App">
      <h2>Voice Activity Detection (VAD) Tool</h2>
      <input type="file" accept=".wav" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Analyze</button>
      {result && (
        <div>
          <h3>VAD Results:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
