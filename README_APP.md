# YellowCert Detection App

A full-stack web application for detecting and analyzing vaccination certificate elements using YOLOv8 object detection.

## Features

- 🤖 **YOLOv8 Object Detection** - Detects 8 different elements on vaccination certificates
- 🎨 **Interactive Web UI** - React-based frontend with real-time visualization
- 📊 **Bounding Box Visualization** - Visual representation of detected elements with confidence scores
- ⚡ **Fast API Backend** - Python FastAPI server for ML inference
- 🎯 **High Accuracy** - Trained on specialized vaccination certificate dataset

## Detected Classes

The model can detect the following elements:
- 💉 Cholera
- 🦠 COVID-19
- 📅 Date
- 🤧 Flu
- 🏥 Logo
- 🧬 Meningococcal
- ✍️ Signature
- 🌍 Yellow Fever

## Project Structure

```
YellowCert/
├── backend/                 # Python FastAPI backend
│   └── main.py             # API server with YOLOv8 inference
├── frontend/               # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styling
│   │   ├── index.js        # React entry point
│   │   └── index.css       # Global styles
│   └── package.json        # Frontend dependencies
├── models/                 # Trained model weights
│   └── best.pt            # Best YOLOv8 model (after training)
├── train/                  # Training dataset
├── valid/                  # Validation dataset
├── test/                   # Test dataset
├── train_model.py         # YOLOv8 training script
├── requirements.txt       # Python dependencies
└── data.yaml             # Dataset configuration

## Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- GPU with CUDA support (recommended for training)

### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Train the YOLOv8 model:

**Option A: Local Training (Mac/PC)**
```bash
python train_model.py
```

**Option B: Google Colab (Recommended - Free GPU!)** 🚀
```bash
# Prepare dataset for Colab
./prepare_for_colab.sh

# Then upload YellowCert_Training_Colab.ipynb to Colab
# See COLAB_TRAINING_GUIDE.md for detailed instructions
```

This will:
- Train YOLOv8 on the vaccination certificate dataset
- Save the best model to `models/best.pt`
- Display training metrics and validation results

**Note:** Google Colab is recommended for faster training with free GPU access!

3. Start the FastAPI server:
```bash
cd backend
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Start the React development server:
```bash
npm start
```

The web app will open at `http://localhost:3000`

## Usage

1. **Start the Backend**:
   ```bash
   cd backend
   python main.py
   ```

2. **Start the Frontend**:
   ```bash
   cd frontend
   npm start
   ```

3. **Upload an Image**:
   - Click "Choose Image" and select a vaccination certificate
   - Click "Detect" to run the model
   - View the results with bounding boxes and confidence scores

## API Endpoints

### `GET /`
Health check endpoint
```json
{
  "message": "YellowCert Detection API",
  "status": "running"
}
```

### `POST /predict`
Upload an image for detection

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `file` (image file)

**Response:**
```json
{
  "success": true,
  "detections": [
    {
      "class": "yellowfever",
      "confidence": 0.88,
      "bbox": {
        "x1": 100,
        "y1": 200,
        "x2": 300,
        "y2": 400
      }
    }
  ],
  "image_size": {
    "width": 1034,
    "height": 690
  }
}
```

## Training Configuration

The model is trained with the following settings:
- **Model**: YOLOv8n (nano) - can be changed to s/m/l/x for better accuracy
- **Epochs**: 100
- **Image Size**: 640x640
- **Batch Size**: 16
- **Optimizer**: Auto (SGD/Adam)
- **Data Augmentation**: Enabled (flip, scale, HSV, mosaic)

Modify `train_model.py` to adjust training parameters.

## Model Performance

After training, check the results in `runs/detect/yellowcert_model/`:
- `weights/best.pt` - Best model weights
- `weights/last.pt` - Last epoch weights
- `results.png` - Training metrics visualization
- `confusion_matrix.png` - Confusion matrix
- `val_batch*_pred.jpg` - Validation predictions

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Ultralytics YOLOv8** - State-of-the-art object detection
- **OpenCV** - Image processing
- **PyTorch** - Deep learning framework

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **Canvas API** - Bounding box visualization

## Customization

### Add New Classes
1. Update `data.yaml` with new class names
2. Add annotations for new classes
3. Retrain the model with `python train_model.py`
4. Update `CLASS_NAMES` in `backend/main.py`
5. Update `CLASS_COLORS` in `frontend/src/App.js`

### Adjust Detection Confidence
In `backend/main.py`, modify the confidence threshold:
```python
results = model(img, conf=0.25)  # Change 0.25 to your desired threshold
```

## Troubleshooting

### Model Not Found
If you see "Model not found" error:
1. Make sure you've run `python train_model.py`
2. Check that `models/best.pt` exists
3. Verify the path in `backend/main.py`

### CORS Issues
If frontend can't connect to backend:
1. Ensure backend is running on port 8000
2. Check CORS settings in `backend/main.py`
3. Verify frontend API URL in `frontend/src/App.js`

### GPU Out of Memory
If training fails due to GPU memory:
1. Reduce batch size in `train_model.py`
2. Use smaller model (yolov8n instead of yolov8s/m/l)
3. Reduce image size

## License

This project uses the YellowCert dataset which is licensed under CC BY 4.0.

## Credits

- Dataset: [YellowCert on Roboflow](https://universe.roboflow.com/vitchakorn/yellowcert)
- Model: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
