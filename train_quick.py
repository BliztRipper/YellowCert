"""
Quick training script for testing (fewer epochs)
"""
from ultralytics import YOLO
import os

def quick_train():
    """Quick training for testing - only 10 epochs"""
    print("Quick training mode - 10 epochs for testing")

    model = YOLO('yolov8n.pt')

    results = model.train(
        data='data.yaml',
        epochs=10,              # Just 10 epochs for quick testing
        imgsz=640,
        batch=8,
        name='yellowcert_quick',
        device='cpu',
        workers=4,
        project='runs/detect',
        exist_ok=True,
        pretrained=True,
        verbose=True,
    )

    # Validate
    metrics = model.val()

    # Export best model
    os.makedirs('models', exist_ok=True)
    best_model_path = 'runs/detect/yellowcert_quick/weights/best.pt'

    if os.path.exists(best_model_path):
        import shutil
        shutil.copy(best_model_path, 'models/best.pt')
        print(f"\n✅ Quick training complete! Model saved to: models/best.pt")
        print(f"Metrics: {metrics}")

if __name__ == "__main__":
    quick_train()
