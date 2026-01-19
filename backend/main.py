from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import os

app = FastAPI()

# Enable CORS for React frontend (development and production)
allowed_origins = [
    "http://localhost:3000",  # Local development
    "http://localhost:3001",  # Alternative local port
]

# Add production origins from environment variable
production_origin = os.getenv("FRONTEND_URL")
if production_origin:
    allowed_origins.append(production_origin)
    # Also allow Vercel preview deployments
    if "vercel.app" in production_origin:
        allowed_origins.append("https://*.vercel.app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "best.pt")
model = None

# Class names from data.yaml
CLASS_NAMES = ['cholera', 'covid', 'date', 'flu', 'logo', 'meningo', 'signature', 'yellowfever']

@app.on_event("startup")
async def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = YOLO(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    else:
        print(f"Warning: Model not found at {MODEL_PATH}. Please train the model first.")
        # Use a pretrained YOLOv8 model as fallback for testing
        model = YOLO('yolov8n.pt')

@app.get("/")
async def root():
    return {"message": "YellowCert Detection API", "status": "running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read image file
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid image file"}
            )

        # Get image dimensions
        height, width = img.shape[:2]

        # Run inference with lower confidence threshold
        results = model(img, conf=0.1)

        # Process results
        detections = []
        for result in results:
            boxes = result.boxes
            print(f"Number of detections: {len(boxes)}")
            for box in boxes:
                # Get box coordinates (xyxy format)
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

                # Get class and confidence
                cls = int(box.cls[0].cpu().numpy())
                conf = float(box.conf[0].cpu().numpy())

                # Get class name
                class_name = CLASS_NAMES[cls] if cls < len(CLASS_NAMES) else f"class_{cls}"

                detections.append({
                    "class": class_name,
                    "confidence": round(conf, 2),
                    "bbox": {
                        "x1": float(x1),
                        "y1": float(y1),
                        "x2": float(x2),
                        "y2": float(y2)
                    }
                })

        return {
            "success": True,
            "detections": detections,
            "image_size": {
                "width": width,
                "height": height
            }
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
