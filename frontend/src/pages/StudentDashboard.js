import React, { useEffect, useState } from "react";
import { API } from "../utils/api";
import ChatBot from "../components/ChatBot";
import ProgressBar from "../components/ProgressBar";

export default function StudentDashboard({ student }) {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState(student.progress);
  const [completedModules, setCompletedModules] = useState(student.completedModules);

  useEffect(() => {
    const fetchModules = async () => {
      const res = await API.get("/modules");
      const filtered = res.data.filter(m => m.branch.includes(student.branch) || m.branch.includes("All"));
      setModules(filtered);
    };
    fetchModules();
  }, []);

  const completeModule = async (moduleId) => {
    const res = await API.post("/modules/complete", { studentId: student.id, moduleId });
    setProgress(res.data.progress);
    setCompletedModules(prev => [...prev, moduleId]);
  };

  const requestApproval = async (moduleId) => {
    try {
      const res = await API.post("/students/request-approval", { studentId: student.id, moduleId });
      alert(res.data.message);
    } catch (err) {
      alert(err.response.data.detail);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Welcome, {student.name}</h2>
      <ProgressBar progress={progress} />
      <p><b>Completed Modules:</b> {completedModules.join(", ") || "None"}</p>

      <h3>Modules</h3>
      {modules.map((m) => (
        <div key={m.id} style={{ border: "1px solid gray", margin: "5px", padding: "5px" }}>
          <h4>{m.title}</h4>
          <iframe width="300" height="200" src={m.youtubeLink} title={m.title}></iframe>
          <br />
          <button onClick={() => completeModule(m.id)}>Mark Complete</button>
          <button onClick={() => requestApproval(m.id)}>Request Approval</button>
        </div>
      ))}

      <ChatBot student={student} />
    </div>
  );
}
