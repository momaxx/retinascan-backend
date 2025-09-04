function ConfidenceMeter({ score }) {
  const color = score < 40 ? '#4caf50' : score < 70 ? '#ff9800' : '#f44336';

  return (
    <div className="confidence-meter">
      <svg width="120" height="120">
        <circle cx="60" cy="60" r="50" stroke="#eee" strokeWidth="10" fill="none" />
        <circle
          cx="60"
          cy="60"
          r="50"
          stroke={color}
          strokeWidth="10"
          fill="none"
          strokeDasharray={`${(score / 100) * 314}, 314`}
          strokeLinecap="round"
          transform="rotate(-90 60 60)"
        />
        <text x="60" y="65" textAnchor="middle" fontSize="18" fill="#333">
          {score}%
        </text>
      </svg>
    </div>
  );
}
