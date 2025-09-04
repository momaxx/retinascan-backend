function GradCAMViewer({ originalSrc, overlaySrc }) {
  const [showOverlay, setShowOverlay] = useState(true);
  const [opacity, setOpacity] = useState(0.5);

  return (
    <div className="gradcam-viewer">
      <div style={{ position: 'relative' }}>
        <img src={originalSrc} alt="Original" style={{ width: '100%' }} />
        {showOverlay && (
          <img
            src={overlaySrc}
            alt="Grad-CAM"
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              opacity,
              pointerEvents: 'none',
            }}
          />
        )}
      </div>
      <div className="controls">
        <label>
          Overlay:
          <input
            type="checkbox"
            checked={showOverlay}
            onChange={() => setShowOverlay(!showOverlay)}
          />
        </label>
        <label>
          Opacity:
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={opacity}
            onChange={(e) => setOpacity(parseFloat(e.target.value))}
          />
        </label>
      </div>
    </div>
  );
}
<ShareQRCode url="https://retinascan-pro.vercel.app" />
