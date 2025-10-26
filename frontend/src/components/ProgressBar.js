import React from "react";

export default function ProgressBar({ progress, height = 20 }) {
  return (
    <div style={{ border: "1px solid #ccc", borderRadius: "5px", width: "100%", height: `${height}px`, marginBottom: "5px" }}>
      <div
        style={{
          width: `${progress}%`,
          backgroundColor: "#4caf50",
          height: "100%",
          borderRadius: "5px",
          textAlign: "center",
          color: "white",
          fontWeight: "bold",
          lineHeight: `${height}px`,
          transition: "width 0.3s"
        }}
      >
        {progress}%
      </div>
    </div>
  );
}
