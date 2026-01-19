"""
YellowCert Model Training - MAXIMUM ACCURACY MODE

This script uses the largest YOLOv8x model with extensive training for absolute maximum accuracy.
⚠️ WARNING: This requires significant GPU memory (16GB+ VRAM recommended) and takes much longer to train.

Use this only if:
- You have a powerful GPU (RTX 3090, RTX 4090, A100, etc.)
- You need the absolute best accuracy
- Training time is not a concern

For most users, train_model.py (YOLOv8m) provides excellent accuracy with reasonable training time.
"""

from ultralytics import YOLO
import os
import torch

def train_max_accuracy():
    """
    Train YOLOv8x model with maximum settings for absolute best accuracy
    """
    print("="*80)
    print("YellowCert Training - MAXIMUM ACCURACY MODE")
    print("="*80)
    print("\n⚠️  WARNING: This mode requires powerful GPU (16GB+ VRAM)")
    print("\nMaximum optimizations enabled:")
    print("  ✓ Model: YOLOv8x (extra-large) - Best possible accuracy")
    print("  ✓ Epochs: 300 with early stopping (patience=100)")
    print("  ✓ Image size: 1280x1280 for maximum detail")
    print("  ✓ Optimizer: AdamW with fine-tuned learning rate")
    print("  ✓ Enhanced data augmentation pipeline")
    print("  ✓ TTA (Test-Time Augmentation) enabled")
    print("  ✓ Multi-scale training")
    print("\n" + "="*80 + "\n")

    if not torch.cuda.is_available():
        print("❌ ERROR: CUDA GPU not detected!")
        print("This training mode requires a CUDA-capable GPU.")
        print("Please use train_model.py for CPU/MPS training instead.")
        return

    device = 0
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB\n")

    # Using YOLOv8x (extra-large) for maximum accuracy
    model = YOLO('yolov8x.pt')

    try:
        results = model.train(
            # Core training parameters - MAXIMUM
            data='data.yaml',
            epochs=300,                 # More epochs for better convergence
            imgsz=1280,                 # Larger image size for more detail
            batch=8,                    # Smaller batch due to larger model
            name='yellowcert_max',
            patience=100,               # Very high patience for best possible model
            save=True,
            device=device,
            workers=8,
            project='runs/detect',
            exist_ok=True,
            pretrained=True,
            verbose=True,
            plots=True,

            # Optimizer settings - fine-tuned for large model
            optimizer='AdamW',
            lr0=0.0005,                 # Lower learning rate for large model
            lrf=0.001,                  # Very low final learning rate
            momentum=0.937,
            weight_decay=0.0005,

            # Enhanced data augmentation
            hsv_h=0.02,
            hsv_s=0.7,
            hsv_v=0.4,
            degrees=15.0,               # More rotation
            translate=0.15,             # More translation
            scale=0.7,                  # More scaling
            shear=2.0,                  # Add some shear
            perspective=0.0005,         # Add perspective
            flipud=0.0,
            fliplr=0.5,
            mosaic=1.0,
            mixup=0.15,                 # More mixup
            copy_paste=0.15,            # More copy-paste

            # Advanced settings - MAXIMUM
            close_mosaic=15,            # Close mosaic later
            amp=True,
            cache=True,
            label_smoothing=0.1,

            # Multi-scale training
            rect=False,                 # Full multi-scale

            # Validation with TTA
            val=True,
            save_period=10,
        )

        # Validate with Test-Time Augmentation for best accuracy
        print("\n" + "="*80)
        print("VALIDATING WITH TEST-TIME AUGMENTATION")
        print("="*80 + "\n")
        metrics = model.val(
            data='data.yaml',
            imgsz=1280,
            batch=4,
            augment=True,               # Enable TTA
        )

        # Save the model
        os.makedirs('models', exist_ok=True)
        best_model_path = 'runs/detect/yellowcert_max/weights/best.pt'

        if os.path.exists(best_model_path):
            import shutil
            shutil.copy(best_model_path, 'models/best_max.pt')
            print("\n" + "="*80)
            print("MAXIMUM ACCURACY TRAINING COMPLETED!")
            print("="*80)
            print(f"\n✓ Best model saved to: models/best_max.pt")
            print(f"✓ All results saved to: runs/detect/yellowcert_max/")
            print(f"\n📊 Final Metrics (with TTA):")
            if hasattr(metrics, 'box'):
                print(f"   - mAP50: {metrics.box.map50:.4f}")
                print(f"   - mAP50-95: {metrics.box.map:.4f}")
                print(f"   - Precision: {metrics.box.mp:.4f}")
                print(f"   - Recall: {metrics.box.mr:.4f}")

            print(f"\n💡 To use this model in the app:")
            print(f"   1. Copy: cp models/best_max.pt models/best.pt")
            print(f"   2. Restart the backend server")

            print(f"\n📈 Training visualizations: runs/detect/yellowcert_max/")
            print("="*80 + "\n")
        else:
            print("\n⚠️ Warning: Best model not found. Check training logs.")

    except RuntimeError as e:
        if "out of memory" in str(e).lower():
            print("\n" + "="*80)
            print("❌ GPU OUT OF MEMORY ERROR")
            print("="*80)
            print("\nSuggestions to fix:")
            print("  1. Reduce batch size (try batch=4 or batch=2)")
            print("  2. Reduce image size (try imgsz=1024 or imgsz=640)")
            print("  3. Use a smaller model in train_model.py (YOLOv8m)")
            print("  4. Close other GPU applications")
            print("  5. Use a GPU with more VRAM")
            print("="*80 + "\n")
        raise

if __name__ == "__main__":
    train_max_accuracy()
