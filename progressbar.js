import "./ProgressBar.css"
const ProgressBar = ({ progress }) => {
  const safeProgress = Math.min(Math.max(progress, 0), 100);

  return (
    <div className="progress-container">
      <div
        className="progress-fill"
        style={{ width: `${safeProgress}%` }}
      >
        <span className="progress-text">{safeProgress}%</span>
      </div>
    </div>
  );
};

export default ProgressBar