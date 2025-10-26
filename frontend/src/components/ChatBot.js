import React, { useState } from "react";
import { API } from "../utils/api";

export default function ChatBot({ student }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    const res = await API.post("/chatbot", { question });
    setAnswer(res.data.answer);
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>ChatBot</h3>
      <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask me..." />
      <button onClick={ask}>Ask</button>
      {answer && <p><b>Answer:</b> {answer}</p>}
    </div>
  );
}
