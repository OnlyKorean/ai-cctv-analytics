import { useState, useEffect } from 'react';

export default function Home() {
  const [stats, setStats] = useState({ total_in: 0, total_out: 0, current: 0, events: [] });

  useEffect(() => {
    // analytics.json yuklash (test uchun)
    fetch('/analytics.json')
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div style={{ padding: '50px', textAlign: 'center', fontFamily: 'Arial' }}>
      <h1>CCTV Analytics Dashboard</h1>
      <div style={{ fontSize: '48px', margin: '30px' }}>
        <p>Kirdi: <strong>{stats.total_in}</strong></p>
        <p>Chiqdi: <strong>{stats.total_out}</strong></p>
        <p>Hozir: <strong>{stats.current}</strong></p>
      </div>
      <h2>Events</h2>
      <ul>
        {stats.events?.map((e, i) => (
          <li key={i}>{e.type} - {e.time}</li>
        ))}
      </ul>
    </div>
  );
}
