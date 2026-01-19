"""
YellowCert Model Training - Optimized for Maximum Accuracy

Key optimizations:
1. Model: YOLOv8m (medium) - Better accuracy than nano, balanced speed
2. Epochs: 200 with early stopping (patience=50)
3. Optimizer: AdamW with optimized learning rate schedule
4. Augmentation: Comprehensive data augmentation (HSV, rotation, mosaic, mixup, copy-paste)
5. Advanced: AMP training, image caching, label smoothing
6. Close mosaic in final 10 epochs for better precision

For even better results (but slower training):
- Change model to 'yolov8l.pt' or 'yolov8x.pt'
- Increase batch size if GPU memory allows
- Increase image size to 1280 if GPU memory allows
"""

from ultralytics import YOLO
import os
import torch

def train_yellowcert_model():
    """
    Train YOLOv8 model on the YellowCert dataset with optimized parameters for maximum accuracy
    """
    print("="*80)
    print("YellowCert Training - OPTIMIZED FOR MAXIMUM RESULTS")
    print("="*80)
    print("\nOptimizations enabled:")
    print("  ✓ Model: YOLOv8m (medium) for better accuracy")
    print("  ✓ Epochs: 200 with early stopping (patience=50)")
    print("  ✓ Optimizer: AdamW with learning rate scheduling")
    print("  ✓ Data Augmentation: HSV, Rotation, Mosaic, MixUp, Copy-Paste")
    print("  ✓ Advanced: AMP training, Image caching, Label smoothing")
    print("  ✓ Close mosaic in final 10 epochs for precision")
    print("\n" + "="*80 + "\n")
    if torch.cuda.is_available():
        device = 0
    else:
        device = 'cpu'

    print(f"Using device: {device}")
    print(f"MPS available: {torch.backends.mps.is_available()}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    # Using YOLOv8m (medium) for better accuracy than nano
    # Options: yolov8n.pt (fastest), yolov8s.pt, yolov8m.pt (balanced), yolov8l.pt, yolov8x.pt (most accurate)
    model = YOLO('yolov8m.pt')

    results = model.train(
        # Core training parameters
        data='data.yaml',           # Path to data configuration
        epochs=200,                 # Increased epochs for better convergence
        imgsz=1024,                 # Image size - matches medical certificate resolution
        batch=16,                   # Increased batch size for better gradient estimates
        name='yellowcert_model',    # Experiment name
        patience=50,                # Increased early stopping patience
        save=True,                  # Save checkpoints
        device=device,              # Auto-detected device
        workers=8,                  # Increased workers for faster data loading
        project='runs/detect',      # Project directory
        exist_ok=True,              # Overwrite existing project
        pretrained=True,            # Use pretrained weights
        verbose=True,               # Verbose output
        plots=True,                 # Save training plots

        # Optimizer settings for better convergence
        optimizer='AdamW',          # AdamW optimizer (better than SGD for many cases)
        lr0=0.001,                  # Initial learning rate
        lrf=0.01,                   # Final learning rate (lr0 * lrf)
        momentum=0.937,             # Momentum
        weight_decay=0.0005,        # Weight decay for regularization

        # Data augmentation for better generalization
        hsv_h=0.015,                # HSV-Hue augmentation
        hsv_s=0.7,                  # HSV-Saturation augmentation
        hsv_v=0.4,                  # HSV-Value augmentation
        degrees=10.0,               # Rotation augmentation (+/- deg)
        translate=0.1,              # Translation augmentation (+/- fraction)
        scale=0.5,                  # Scaling augmentation (+/- gain)
        shear=0.0,                  # Shear augmentation (+/- deg)
        perspective=0.0,            # Perspective augmentation (+/- fraction)
        flipud=0.0,                 # Flip up-down probability
        fliplr=0.5,                 # Flip left-right probability
        mosaic=1.0,                 # Mosaic augmentation probability
        mixup=0.1,                  # MixUp augmentation probability
        copy_paste=0.1,             # Copy-paste augmentation probability

        # Advanced settings
        close_mosaic=10,            # Disable mosaic augmentation in final N epochs for better precision
        amp=True,                   # Automatic Mixed Precision training (faster on modern GPUs)
        cache=True,                 # Cache images for faster training
        label_smoothing=0.1,        # Label smoothing for better generalization

        # Validation settings
        val=True,                   # Validate during training
        save_period=10,             # Save checkpoint every N epochs
    )

    # Validate the final model
    print("\n" + "="*80)
    print("VALIDATING FINAL MODEL")
    print("="*80 + "\n")
    metrics = model.val()

    # Save the best model
    os.makedirs('models', exist_ok=True)
    best_model_path = 'runs/detect/yellowcert_model/weights/best.pt'

    if os.path.exists(best_model_path):
        import shutil
        shutil.copy(best_model_path, 'models/best.pt')
        print("\n" + "="*80)
        print("TRAINING COMPLETED SUCCESSFULLY!")
        print("="*80)
        print(f"\n✓ Best model saved to: models/best.pt")
        print(f"✓ All results saved to: runs/detect/yellowcert_model/")
        print(f"\n📊 Final Metrics:")
        if hasattr(metrics, 'box'):
            print(f"   - mAP50: {metrics.box.map50:.4f}")
            print(f"   - mAP50-95: {metrics.box.map:.4f}")
        print(f"\n💡 To use this model in the app, it's ready at: models/best.pt")
        print(f"\n📈 Check training plots at: runs/detect/yellowcert_model/")
        print("="*80 + "\n")
    else:
        print("\n⚠️ Warning: Best model not found. Check training logs.")

if __name__ == "__main__":
    train_yellowcert_model()
