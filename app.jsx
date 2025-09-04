import { useState } from 'react';
import ImageUploader from './components/ImageUploader';
import ConfidenceMeter from './components/ConfidenceMeter';
import GradCAMViewer from './components/GradCAMViewer';

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [gradcam, setGradcam] = useState(null);

  const handleUpload = async (file) => {
    setImage(file);
    const previewURL = URL.createObjectURL(file);
    setPreview(previewURL);

    // Send to backend
    const formData = new FormData();
    formData.append('image', file);
    const res = await fetch('https://your-api-endpoint.com/analyze', {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    setConfidence(data.confidence);
    setGradcam(data.gradcam_url); // Assuming backend returns Grad-CAM image URL
  };

  return (
    <div className="retinascan-app">
      <h1>RetinaScan Pro</h1>
      <ImageUploader onUpload={handleUpload} />
      {preview && <GradCAMViewer originalSrc={preview} overlaySrc={gradcam} />}
      {confidence !== null && <ConfidenceMeter score={confidence} />}
    </div>
  );
}
