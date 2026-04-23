import { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);
  
  // Backend states
  const [detectedIntent, setDetectedIntent] = useState("");
  const [attempts, setAttempts] = useState(0);
  const [copied, setCopied] = useState(false);
  
  // 🌟 NEW STATES FOR DUAL ENGINE
  const [aiMode, setAiMode] = useState("local"); // Default is local SLM
  const [engineUsed, setEngineUsed] = useState("");

  const generateCode = async () => {
    setLoading(true);
    setCode("");
    setDetectedIntent("");
    setEngineUsed("");
    setCopied(false);

    try {
      const response = await fetch("http://127.0.0.1:8000/generate-code", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // 🌟 Send 'mode' to backend
        body: JSON.stringify({ prompt: prompt, mode: aiMode }),
      });

      const data = await response.json();
      
      setCode(data.generated_code);
      setDetectedIntent(data.detected_intent);
      setAttempts(data.attempts_taken);
      setEngineUsed(data.engine_used); // Update engine badge
      
    } catch (error) {
      setCode("Error connecting to backend");
    }

    setLoading(false);
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    
    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  return (
    <div className="app-wrapper">
      <div className="app-card">
        <h2 className="app-title">CogniCode AI Generator</h2>

        <textarea
          rows="4"
          className="prompt-input"
          placeholder="e.g., sort this array of numbers in descending order..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <br /><br />

        {/* 🌟 NEW DUAL ENGINE TOGGLE SWITCH */}
        <div style={{ display: "flex", gap: "10px", marginBottom: "20px", justifyContent: "center" }}>
          <button
            onClick={() => setAiMode("local")}
            style={{
              padding: "10px 20px",
              borderRadius: "8px",
              border: aiMode === "local" ? "2px solid #3b82f6" : "1px solid #4b5563",
              backgroundColor: aiMode === "local" ? "rgba(59, 130, 246, 0.2)" : "transparent",
              color: aiMode === "local" ? "#fff" : "#9ca3af",
              cursor: "pointer",
              fontWeight: "bold",
              transition: "all 0.3s"
            }}
          >
            🔒 Local SLM Mode
          </button>
          
          <button
            onClick={() => setAiMode("gemini")}
            style={{
              padding: "10px 20px",
              borderRadius: "8px",
              border: aiMode === "gemini" ? "2px solid #10b981" : "1px solid #4b5563",
              background: aiMode === "gemini" ? "rgba(16, 185, 129, 0.2)" : "transparent",
              color: aiMode === "gemini" ? "#fff" : "#9ca3af",
              cursor: "pointer",
              fontWeight: "bold",
              transition: "all 0.3s"
            }}
          >
             Cloud Model
          </button>
        </div>

        <button 
          onClick={generateCode}
          disabled={loading || !prompt}
          className="generate-btn"
        >
          {loading ? "Generating & Validating..." : "Generate Code"}
        </button>

        {/* AI Intelligence Dashboard */}
        {detectedIntent && (
          <div className="dashboard-container" style={{ marginTop: "20px", display: "flex", gap: "10px", flexWrap: "wrap", justifyContent: "center" }}>
            {/* Engine Badge */}
            {engineUsed && (
              <span className="badge" style={{ backgroundColor: "#4f46e5", color: "white", padding: "5px 10px", borderRadius: "5px", fontSize: "0.85rem", fontWeight: "bold" }}>
                ⚙️ {engineUsed}
              </span>
            )}

            <span className="badge badge-intent" style={{ backgroundColor: "#3b82f6", color: "white", padding: "5px 10px", borderRadius: "5px", fontSize: "0.85rem", fontWeight: "bold" }}>
              🎯 Intent: {detectedIntent}
            </span>

            <span className={`badge ${attempts === 1 ? 'badge-success' : 'badge-warning'}`} style={{ backgroundColor: attempts === 1 ? "#10b981" : "#f59e0b", color: "white", padding: "5px 10px", borderRadius: "5px", fontSize: "0.85rem", fontWeight: "bold" }}>
              {aiMode === "gemini" 
                ? "⚡ Cloud Generated" 
                : (attempts === 1 ? "⚡ Validated on First Try" : `🔄 Auto-Corrected (${attempts} attempts)`)}
            </span>
          </div>
        )}

        {/* Code Display Area */}
        {code && (
          <div className="code-wrapper">
            {/* Terminal Header */}
            <div className="code-header">
              <div className="mac-dots">
                <div className="dot dot-red"></div>
                <div className="dot dot-yellow"></div>
                <div className="dot dot-green"></div>
              </div>
              
              <button 
                onClick={handleCopy}
                className={`copy-btn ${copied ? 'copied' : ''}`}
              >
                {copied ? "✅ Copied" : "📋 Copy"}
              </button>
            </div>

            <pre className="code-block">
              {code}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;