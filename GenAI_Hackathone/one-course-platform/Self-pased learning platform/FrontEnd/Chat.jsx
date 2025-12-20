 Chat.jsx

import { useState } from "react";
import { sendPrompt } from "../api";

export default function Chat() {
  const [q, setQ] = useState("");
  const [a, setA] = useState("");

  const ask = async () => {
    const res = await sendPrompt(q);
    setA(res.response);
  };

  return (
    <div>
      <textarea onChange={e => setQ(e.target.value)} />
      <button onClick={ask}>Ask AI Tutor</button>
      <p>{a}</p>
    </div>
  );
}