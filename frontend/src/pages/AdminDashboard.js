import React, { useEffect, useState } from "react";
import { API } from "../utils/api";
import ProgressBar from "../components/ProgressBar";

export default function AdminDashboard({ admin }) {
  const [students, setStudents] = useState([]);
  const [requests, setRequests] = useState([]);

  const fetchStudents = async () => {
    const res = await API.get("/students/all");
    setStudents(res.data);
  };

  const fetchPending = async () => {
    const res = await API.get("/students/pending-approvals");
    setRequests(res.data);
  };

  useEffect(() => {
    fetchStudents();
    fetchPending();
  }, []);

  const handleApproval = async (id, approve) => {
    const res = await API.post("/students/handle-approval", { requestId: id, approve });
    alert(res.data.message);
    fetchPending();
    fetchStudents();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Welcome, {admin.name}</h2>

      <h3>Student Progress</h3>
      {students.map((s) => (
        <div key={s.id} style={{ border: "1px solid gray", margin: "5px", padding: "5px" }}>
          <p><b>Name:</b> {s.name}</p>
          <p><b>Email:</b> {s.email}</p>
          <p><b>Branch:</b> {s.branch}</p>
          <p><b>Career Interest:</b> {s.careerInterest}</p>
          <ProgressBar progress={s.progress} height={15} />
          <p><b>Completed Modules:</b> {s.completedModules.join(", ") || "None"}</p>
        </div>
      ))}

      <h3>Pending Approvals</h3>
      {requests.length === 0 ? <p>No pending requests</p> :
        requests.map((r) => (
          <div key={r.id} style={{ border: "1px solid gray", margin: "5px", padding: "5px" }}>
            <p><b>Student:</b> {r.studentName}</p>
            <p><b>Module ID:</b> {r.moduleId}</p>
            <button onClick={() => handleApproval(r.id, true)}>Approve</button>
            <button onClick={() => handleApproval(r.id, false)}>Reject</button>
          </div>
        ))}
    </div>
  );
}
