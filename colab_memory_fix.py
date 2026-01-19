"""
Colab Memory Fix - Add this to your notebook to prevent OOM errors

Copy this entire cell and run it BEFORE your training cell in Colab
"""

import gc
import torch

print("="*80)
print("🔧 APPLYING MEMORY OPTIMIZATIONS FOR T4 GPU")
print("="*80)

# 1. Clear existing GPU memory
gc.collect()
if torch.cuda.is_available():
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats()
    print("✓ GPU memory cleared")

# 2. Check available memory
if torch.cuda.is_available():
    total_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"✓ Total GPU VRAM: {total_memory:.1f} GB")

    # 3. Auto-detect if we need to optimize
    if total_memory < 16:  # T4 GPU
        print("\n⚠️  T4 GPU detected (15GB VRAM)")
        print("   Applying memory-safe settings...\n")

        # 4. Update config for memory efficiency
        if 'config' in globals():
            original_batch = config.get('batch', 16)
            original_imgsz = config.get('imgsz', 1024)
            original_model = config.get('model', 'yolov8m.pt')

            # Optimize settings
            if config['model'] == 'yolov8m.pt' and config['imgsz'] >= 1024:
                # YOLOv8m with large images - reduce both
                config['batch'] = min(config['batch'], 8)
                config['imgsz'] = 640
                print(f"✓ Batch size: {original_batch} → {config['batch']}")
                print(f"✓ Image size: {original_imgsz} → {config['imgsz']}")

            elif config['model'] == 'yolov8m.pt':
                # YOLOv8m with smaller images - reduce batch
                config['batch'] = min(config['batch'], 8)
                print(f"✓ Batch size: {original_batch} → {config['batch']}")

            elif config['imgsz'] >= 1024:
                # Large images - reduce size or batch
                if config['batch'] > 16:
                    config['batch'] = 16
                    print(f"✓ Batch size: {original_batch} → {config['batch']}")
                config['imgsz'] = min(config['imgsz'], 640)
                print(f"✓ Image size: {original_imgsz} → {config['imgsz']}")

            # Use smaller model if still too large
            if config['model'] in ['yolov8l.pt', 'yolov8x.pt']:
                config['model'] = 'yolov8m.pt'
                print(f"✓ Model: {original_model} → {config['model']}")
                print("  (Large/XL models don't fit in T4 GPU)")

            print(f"\n✓ Final settings:")
            print(f"  Model: {config['model']}")
            print(f"  Image size: {config['imgsz']}")
            print(f"  Batch size: {config['batch']}")
        else:
            print("⚠️  Config not found - create it first")
            print("\nRecommended T4 settings:")
            print("  model: yolov8s.pt")
            print("  imgsz: 640")
            print("  batch: 16")
else:
    print("❌ No GPU detected!")

print("\n" + "="*80)
print("✓ Memory optimization complete - ready to train!")
print("="*80)

# 5. Optional: Set PyTorch memory allocator settings
import os
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
print("\n💡 Tip: If you still get OOM, reduce batch size further")
print("   Add this before training: config['batch'] = 4")
print("="*80)
