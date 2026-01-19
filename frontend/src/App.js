import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css';

// Use environment variable for production, fallback to localhost for development
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Color mapping for different classes - Distinct medical theme colors for easy identification
const CLASS_COLORS = {
  'cholera': '#26A69A',      // Teal - Water/hygiene related
  'covid': '#2196F3',        // Bright Blue - Distinct medical blue
  'date': '#9C27B0',         // Purple - Administrative/documentation
  'flu': '#4CAF50',          // Green - Health/wellness
  'logo': '#1565C0',         // Navy Blue - Professional/official
  'meningo': '#E91E63',      // Pink/Magenta - Alert/important
  'signature': '#5E35B1',    // Indigo - Authority/validation
  'yellowfever': '#FF9800'   // Orange/Amber - Yellow fever specific
};

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [detections, setDetections] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const canvasRef = useRef(null);
  const imageRef = useRef(null);

  const handleImageSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setImagePreview(URL.createObjectURL(file));
      setDetections([]);
      setError(null);
    }
  };

  const handleUpload = async () => {
    console.log('Detect button clicked');
    if (!selectedImage) {
      setError('Please select an image first');
      return;
    }

    console.log('Starting upload...', selectedImage.name);
    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', selectedImage);

    try {
      const response = await axios.post(`${API_URL}/predict`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('Response received:', response.data);

      if (response.data.success) {
        console.log('Detections:', response.data.detections);
        setDetections(response.data.detections);
      } else {
        setError('Detection failed');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to connect to server');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (imagePreview && detections.length > 0 && canvasRef.current && imageRef.current) {
      drawDetections();
    }
  }, [detections, imagePreview]);

  const drawDetections = () => {
    const canvas = canvasRef.current;
    const image = imageRef.current;
    const ctx = canvas.getContext('2d');

    // Set canvas size to match image
    canvas.width = image.naturalWidth;
    canvas.height = image.naturalHeight;

    // Draw image
    ctx.drawImage(image, 0, 0);

    // Draw detections
    detections.forEach((detection) => {
      const { bbox, class: className, confidence } = detection;
      const color = CLASS_COLORS[className] || '#00FF00';

      // Draw bounding box
      ctx.strokeStyle = color;
      ctx.lineWidth = 3;
      ctx.strokeRect(
        bbox.x1,
        bbox.y1,
        bbox.x2 - bbox.x1,
        bbox.y2 - bbox.y1
      );

      // Draw label background
      const label = `${className} ${confidence}`;
      ctx.font = 'bold 16px Arial';
      const textWidth = ctx.measureText(label).width;
      const textHeight = 20;

      ctx.fillStyle = color;
      ctx.fillRect(bbox.x1, bbox.y1 - textHeight - 4, textWidth + 10, textHeight + 4);

      // Draw label text
      ctx.fillStyle = '#000000';
      ctx.fillText(label, bbox.x1 + 5, bbox.y1 - 8);
    });
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>⚕️ YellowCert Medical Analysis</h1>
          <p>AI-Powered Vaccination Certificate Detection System</p>
        </header>

        <div className="upload-section">
          <div className="file-input-wrapper">
            <input
              type="file"
              id="file-input"
              accept="image/*"
              onChange={handleImageSelect}
              className="file-input"
            />
            <label htmlFor="file-input" className="file-input-label">
              📋 Upload Certificate
            </label>
            {selectedImage && <span className="file-name">{selectedImage.name}</span>}
          </div>

          <button
            onClick={handleUpload}
            disabled={!selectedImage || loading}
            className="upload-button"
          >
            {loading ? '⏳ Analyzing...' : '🔬 Analyze Certificate'}
          </button>
        </div>

        {error && (
          <div className="error-message">
            ⚠️ {error}
          </div>
        )}

        {imagePreview && (
          <div className="results-section">
            <div className="image-container">
              <img
                ref={imageRef}
                src={imagePreview}
                alt="Preview"
                style={{ display: detections.length > 0 ? 'none' : 'block' }}
                className="preview-image"
              />
              <canvas
                ref={canvasRef}
                style={{ display: detections.length > 0 ? 'block' : 'none' }}
                className="detection-canvas"
              />
            </div>

            {detections.length > 0 && (
              <div className="detections-list">
                <h3>🩺 Medical Elements Detected ({detections.length})</h3>
                <div className="detection-items">
                  {detections.map((detection, index) => (
                    <div
                      key={index}
                      className="detection-item"
                      style={{ borderLeftColor: CLASS_COLORS[detection.class] }}
                    >
                      <div className="detection-class">
                        <span
                          className="color-indicator"
                          style={{ backgroundColor: CLASS_COLORS[detection.class] }}
                        ></span>
                        {detection.class}
                      </div>
                      <div className="detection-confidence">
                        {(detection.confidence * 100).toFixed(0)}%
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {!imagePreview && (
          <div className="placeholder">
            <div className="placeholder-icon">💉</div>
            <p>Upload a vaccination certificate for medical analysis</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
