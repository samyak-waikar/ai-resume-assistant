import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await axios.post("http://127.0.0.1:8000/upload", formData);
    alert("Resume uploaded successfully!");
  };

  const handleAsk = async () => {
  setLoading(true);
  const res = await axios.post("http://127.0.0.1:8000/ask", null, {
    params: { query },
  });
  setAnswer(res.data.answer);
  setLoading(false);
};

return (
  <div style={{
    minHeight: "100vh",
    background: "#0f172a", // dark background
    padding: "40px"
  }}>
    
    <div style={{
      maxWidth: "900px",
      margin: "auto",
      background: "#111827",
      padding: "30px",
      borderRadius: "12px",
      boxShadow: "0 10px 30px rgba(0,0,0,0.4)",
      color: "white"
    }}>

      <h1 style={{ textAlign: "center", marginBottom: "30px" }}>
        🤖 AI Resume Assistant
      </h1>

      {/* Upload Section */}
      <div style={{ marginBottom: "25px" }}>
        <label style={{ color: "#9ca3af" }}>Upload Resume</label>
        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])}
          style={{ marginTop: "10px", color: "white" }}
        />
        <button 
          onClick={handleUpload}
          style={{
            marginTop: "10px",
            width: "100%",
            padding: "12px",
            background: "#6366f1",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            fontWeight: "bold"
          }}
        >
          Upload Resume
        </button>
      </div>

      {/* Ask Section */}
      <div style={{ marginBottom: "25px" }}>
        <label style={{ color: "#9ca3af" }}>Ask a Question</label>
        <input
          type="text"
          placeholder="e.g. What are my skills?"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            marginTop: "10px",
            borderRadius: "8px",
            border: "1px solid #374151",
            background: "#1f2933",
            color: "white"
          }}
        />
        <button 
          onClick={handleAsk}
          style={{
            marginTop: "10px",
            width: "100%",
            padding: "12px",
            background: "#22c55e",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            fontWeight: "bold"
          }}
        >
          Ask AI
        </button>
      </div>

      {/* Answer Section */}
      <div style={{
        background: "#1f2937",
        padding: "15px",
        borderRadius: "8px",
        minHeight: "100px"
      }}>
        <strong style={{ color: "#9ca3af" }}>Answer:</strong>
        <div style={{ whiteSpace: "pre-wrap", marginTop: "8px" }}>
          {answer || "Your answer will appear here..."}
        </div>
      </div>

    </div>
  </div>
);
}

export default App;