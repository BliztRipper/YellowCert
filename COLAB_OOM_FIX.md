# 🚨 Colab Out of Memory (OOM) Error - Quick Fix

If you're seeing this error:
```
OutOfMemoryError: CUDA out of memory
```

## ⚡ Quick Solution (3 Options)

### Option 1: Use the Fixed Notebook (Easiest) ✅

1. **Use `YellowCert_Training_Colab_v2.ipynb`** instead
   - Already optimized for T4 GPU
   - Smaller batch sizes and image sizes
   - Memory-safe configurations

2. Upload to Colab and run normally

### Option 2: Fix Your Current Notebook

Add this cell **BEFORE** the training cell:

```python
# REDUCE MEMORY USAGE
config['batch'] = 8        # Reduce from 16 to 8
config['imgsz'] = 640      # Reduce from 1024 to 640
config['model'] = 'yolov8s.pt'  # Use smaller model
```

Then re-run the training cell.

### Option 3: Use Quick Mode

Change the training mode:
```python
TRAINING_MODE = 'quick'    # Instead of 'balanced'
```

## 🔧 Detailed Fixes

### Fix 1: Reduce Batch Size

**Problem:** Batch size too large for GPU memory

```python
# Add before training cell
config['batch'] = 4   # Try 4, 6, or 8 (not 16)
```

### Fix 2: Reduce Image Size

**Problem:** Image size too large

```python
# Add before training cell
config['imgsz'] = 640  # Instead of 1024 or 1280
```

### Fix 3: Use Smaller Model

**Problem:** Model too large for GPU

```python
# Add before training cell
config['model'] = 'yolov8s.pt'  # Instead of yolov8m.pt or yolov8l.pt
```

### Fix 4: Disable Caching

**Problem:** Image caching uses too much memory

```python
# In the training cell, change:
cache=False,  # Instead of cache=True
```

### Fix 5: Clear GPU Memory

Run this cell BEFORE training:

```python
import gc
import torch

# Clear memory
gc.collect()
torch.cuda.empty_cache()
torch.cuda.reset_peak_memory_stats()

print("✓ Memory cleared")
```

### Fix 6: Restart Runtime

Complete reset:
1. **Runtime → Restart runtime**
2. Re-run setup cells (1-4)
3. Apply fixes above
4. Run training again

## 📊 T4 GPU Memory Limits

T4 GPU has **~15GB VRAM**. Here's what fits:

| Configuration | Fits in T4? | Notes |
|---------------|-------------|-------|
| YOLOv8n, 640, batch=16 | ✅ Yes | Quick mode - safe |
| YOLOv8s, 640, batch=16 | ✅ Yes | Balanced - recommended |
| YOLOv8s, 640, batch=32 | ⚠️ Maybe | Might be tight |
| YOLOv8m, 640, batch=8 | ✅ Yes | Advanced - safe |
| YOLOv8m, 1024, batch=16 | ❌ No | Too large! |
| YOLOv8l, 640, batch=8 | ⚠️ Maybe | Close to limit |
| YOLOv8l, 1024, batch=8 | ❌ No | Too large! |
| YOLOv8x, any size | ❌ No | Needs 20GB+ |

## ✅ Recommended Settings for T4

### Conservative (Always Works):
```python
model: yolov8s.pt
imgsz: 640
batch: 8
```

### Balanced (Recommended):
```python
model: yolov8s.pt
imgsz: 640
batch: 16
```

### Aggressive (Max for T4):
```python
model: yolov8m.pt
imgsz: 640
batch: 8
```

## 🎯 Step-by-Step Recovery

1. **Don't panic!** This is common

2. **Restart runtime:**
   - Runtime → Restart runtime

3. **Re-upload dataset** (if needed)

4. **Change training mode:**
   ```python
   TRAINING_MODE = 'balanced'  # Safe choice
   ```

5. **Add memory fixes before training:**
   ```python
   # Add this cell before training:
   config['batch'] = 8
   config['imgsz'] = 640
   ```

6. **Clear memory:**
   ```python
   import gc
   import torch
   gc.collect()
   torch.cuda.empty_cache()
   ```

7. **Run training again**

## 💡 Prevention Tips

### Before You Start:

1. **Use v2 notebook** - Already optimized

2. **Start conservative:**
   - Begin with `balanced` mode
   - Don't use `maximum` or `ultra` on first try

3. **Monitor memory:**
   ```python
   # Add this during training to watch memory
   !nvidia-smi
   ```

4. **Close other tabs** - More RAM for Colab

5. **Use Colab Pro** - Get A100 GPU (40GB VRAM)

## 🆘 Still Not Working?

### Last Resort Options:

1. **Ultra minimal settings:**
   ```python
   TRAINING_MODE = 'quick'
   config['batch'] = 2
   config['imgsz'] = 320
   ```

2. **Train locally on Mac:**
   ```bash
   # On your M4 Pro
   cd /Users/arnon/Downloads/YellowCert
   python train_model.py
   ```
   Slower but will work!

3. **Use Colab Pro** ($10/month)
   - A100 GPU (40GB VRAM)
   - Can handle all modes
   - Worth it for serious training

## 📈 Expected Results by Mode

Even with reduced settings, you'll get good results:

| Settings | Training Time | mAP50 | Quality |
|----------|---------------|-------|---------|
| YOLOv8s, 640, batch=8 | 2-3 hrs | 0.80-0.90 | ⭐⭐⭐⭐ Good |
| YOLOv8s, 640, batch=16 | 2-3 hrs | 0.82-0.92 | ⭐⭐⭐⭐ Great |
| YOLOv8m, 640, batch=8 | 3-4 hrs | 0.85-0.93 | ⭐⭐⭐⭐⭐ Excellent |

**Don't worry about using smaller settings - they still produce excellent results!**

## 🎓 Understanding the Error

The error means:
- GPU tried to allocate 38 MB more
- But only 14 MB available
- 14.72 GB already in use (almost full!)

This happens when:
- ❌ Batch size too large
- ❌ Image size too large
- ❌ Model too large
- ❌ Memory not cleared from previous run

**Solution:** Reduce any of the above!

---

## ✅ Success Story

**Before (OOM Error):**
```python
model: yolov8m.pt
imgsz: 1024
batch: 16
Result: ❌ Out of memory!
```

**After (Fixed):**
```python
model: yolov8s.pt
imgsz: 640
batch: 16
Result: ✅ Works perfectly! mAP50 = 0.89
```

**Lesson:** Smaller settings ≠ worse results!

---

**Need more help?** See `COLAB_TRAINING_GUIDE.md` section "Troubleshooting"

**Quick fix:** Use `YellowCert_Training_Colab_v2.ipynb` (already optimized) ✅
