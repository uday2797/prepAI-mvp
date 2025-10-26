import React, { useState } from "react";
import Login from "./pages/Login";
import StudentDashboard from "./pages/StudentDashboard";
import AdminDashboard from "./pages/AdminDashboard";

export default function App() {
  const [user, setUser] = useState(null);

  if (!user) {
    return <Login setUser={setUser} />;
  }

  if (user.branch) {
    return <StudentDashboard student={user} />;
  } else {
    return <AdminDashboard admin={user} />;
  }
}
