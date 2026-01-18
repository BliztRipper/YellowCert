from ultralytics import YOLO
import os
import torch

def train_yellowcert_model():
    """
    Train YOLOv8 model on the YellowCert dataset
    """
    if torch.cuda.is_available():
        device = 0  
    else:
        device = 'cpu'  

    print(f"Using device: {device}")
    print(f"MPS available: {torch.backends.mps.is_available()}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    model = YOLO('yolov8n.pt')

    results = model.train(
        data='data.yaml',           # Path to data configuration
        epochs=100,                   # Number of training epochs (reduced for faster training)
        imgsz=1024,                   # Image size
        batch=8,                     # Batch size (reduced for CPU training)
        name='yellowcert_model',     # Experiment name
        patience=20,                 # Early stopping patience
        save=True,                   # Save checkpoints
        device=device,               # Auto-detected device
        workers=4,                   # Number of worker threads (reduced for CPU)
        project='runs/detect',       # Project directory
        exist_ok=True,               # Overwrite existing project
        pretrained=True,             # Use pretrained weights
        verbose=True,                # Verbose output
        plots=True,                  # Save training plots
    )

    metrics = model.val()

    os.makedirs('models', exist_ok=True)
    best_model_path = 'runs/detect/yellowcert_model/weights/best.pt'

    if os.path.exists(best_model_path):
        import shutil
        shutil.copy(best_model_path, 'models/best.pt')
        print(f"\nBest model saved to: models/best.pt")

    print("\nTraining completed!")
    print(f"Model metrics: {metrics}")
    print(f"\nTo use the model in the app, the best weights are at: models/best.pt")

if __name__ == "__main__":
    train_yellowcert_model()
