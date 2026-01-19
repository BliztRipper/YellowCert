"""
YellowCert Backend API
Medical certificate detection using YOLOv8
"""

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
import os
from typing import List, Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="YellowCert Detection API",
    description="AI-powered vaccination certificate detection",
    version="1.0.0"
)

# Configure CORS
def get_allowed_origins() -> List[str]:
    """Get list of allowed CORS origins"""
    origins = [
        "http://localhost:3000",  # Local development
        "http://localhost:3001",  # Alternative local port
    ]

    # Add production origin from environment
    production_origin = os.getenv("FRONTEND_URL")
    if production_origin:
        origins.append(production_origin)
        # Allow Vercel preview deployments
        if "vercel.app" in production_origin:
            origins.append("https://*.vercel.app")

    return origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model configuration
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "best.pt")
model = None

# Class names (from data.yaml)
CLASS_NAMES = [
    'cholera', 'covid', 'date', 'flu',
    'logo', 'meningo', 'signature', 'yellowfever'
]

@app.on_event("startup")
async def load_model():
    """Load YOLOv8 model on startup"""
    global model

    try:
        if os.path.exists(MODEL_PATH):
            model = YOLO(MODEL_PATH)
            print(f"✅ Model loaded successfully from {MODEL_PATH}")
        else:
            print(f"⚠️  Warning: Custom model not found at {MODEL_PATH}")
            print(f"⚠️  Using pretrained YOLOv8n model as fallback")
            model = YOLO('yolov8n.pt')
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        raise

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "YellowCert Detection API",
        "status": "running",
        "version": "1.0.0",
        "model_loaded": model is not None
    }

def process_detection(box, class_names: List[str]) -> Dict[str, Any]:
    """Process a single detection box"""
    # Get box coordinates (xyxy format)
    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

    # Get class and confidence
    cls = int(box.cls[0].cpu().numpy())
    conf = float(box.conf[0].cpu().numpy())

    # Get class name
    class_name = class_names[cls] if cls < len(class_names) else f"class_{cls}"

    return {
        "class": class_name,
        "confidence": round(conf, 2),
        "bbox": {
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2)
        }
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Detect medical certificate elements in uploaded image

    Args:
        file: Image file (JPG, PNG, etc.)

    Returns:
        JSON with detections, bounding boxes, and confidence scores
    """
    try:
        # Read and decode image
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": "Invalid image file. Please upload a valid image."
                }
            )

        # Get image dimensions
        height, width = img.shape[:2]

        # Run inference
        results = model(img, conf=0.1)

        # Process detections
        detections = []
        for result in results:
            boxes = result.boxes
            print(f"✓ Detected {len(boxes)} objects")

            for box in boxes:
                detection = process_detection(box, CLASS_NAMES)
                detections.append(detection)

        return {
            "success": True,
            "detections": detections,
            "count": len(detections),
            "image_size": {
                "width": width,
                "height": height
            }
        }

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": f"Prediction failed: {str(e)}"
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
