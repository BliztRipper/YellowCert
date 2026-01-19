# YellowCert Training Guide

This guide explains the different training options available and helps you choose the right one for your needs.

## 📊 Training Scripts Comparison

| Script | Model | Epochs | Accuracy | Speed | GPU Required | Use Case |
|--------|-------|--------|----------|-------|--------------|----------|
| `train_quick.py` | YOLOv8n | 10 | ⭐ | ⚡⚡⚡ | No (CPU OK) | Quick testing |
| `train_model.py` | YOLOv8m | 200 | ⭐⭐⭐⭐ | ⚡⚡ | Recommended | **Production** (Best balance) |
| `train_max_accuracy.py` | YOLOv8x | 300 | ⭐⭐⭐⭐⭐ | ⚡ | Yes (16GB+) | Maximum accuracy |

## 🎯 Which Script Should I Use?

### For Most Users: `train_model.py` ✅ **RECOMMENDED**

```bash
python train_model.py
```

**Best for:** Production deployments, balanced accuracy and speed

**Features:**
- ✅ YOLOv8m (medium) model - excellent accuracy
- ✅ 200 epochs with early stopping
- ✅ AdamW optimizer with learning rate scheduling
- ✅ Comprehensive data augmentation
- ✅ Works on consumer GPUs (8GB+ VRAM)
- ✅ Optimized training time (~2-4 hours on RTX 3080)

**Expected Results:**
- mAP50: 0.85-0.95
- mAP50-95: 0.70-0.85
- Good real-time performance

---

### For Quick Testing: `train_quick.py`

```bash
python train_quick.py
```

**Best for:** Testing the pipeline, debugging, quick iterations

**Features:**
- ⚡ Fast training (10 epochs only)
- ⚡ Small model (YOLOv8n)
- ⚡ Works on CPU (slow) or any GPU
- ⚡ Completes in ~10-30 minutes

**Expected Results:**
- mAP50: 0.60-0.75
- Good for testing, not for production

---

### For Maximum Accuracy: `train_max_accuracy.py`

```bash
python train_max_accuracy.py
```

**Best for:** Research, competitions, absolute best results

**Requirements:**
- ⚠️ Powerful GPU with 16GB+ VRAM (RTX 3090, RTX 4090, A100)
- ⚠️ Long training time (6-12 hours)
- ⚠️ CUDA required (won't work on CPU/MPS)

**Features:**
- 🏆 YOLOv8x (extra-large) - largest model
- 🏆 300 epochs with extended patience
- 🏆 1280x1280 image size
- 🏆 Enhanced augmentation pipeline
- 🏆 Test-Time Augmentation (TTA) validation

**Expected Results:**
- mAP50: 0.90-0.98
- mAP50-95: 0.75-0.90
- Slower inference but best accuracy

---

## 🚀 Training Optimizations Explained

### Model Size Impact

| Model | Parameters | Speed | Accuracy | VRAM |
|-------|-----------|-------|----------|------|
| YOLOv8n | 3.2M | Fastest | Good | 2GB |
| YOLOv8s | 11.2M | Fast | Better | 4GB |
| **YOLOv8m** | **25.9M** | **Balanced** | **Great** | **8GB** |
| YOLOv8l | 43.7M | Slower | Excellent | 12GB |
| YOLOv8x | 68.2M | Slowest | Best | 16GB |

### Key Optimizations in `train_model.py`

1. **AdamW Optimizer**
   - Better convergence than SGD for many cases
   - Adaptive learning rates per parameter
   - Built-in weight decay

2. **Data Augmentation**
   - HSV color jittering (lighting variations)
   - Rotation, translation, scaling (geometric variations)
   - Mosaic (combine 4 images - learn context)
   - MixUp (blend 2 images - better generalization)
   - Copy-paste (augment object instances)

3. **Close Mosaic**
   - Disable mosaic in final 10 epochs
   - Allows model to learn on normal images
   - Improves final accuracy

4. **Label Smoothing**
   - Prevents overconfidence
   - Better generalization
   - Reduces overfitting

5. **AMP Training**
   - Automatic Mixed Precision
   - Faster training on modern GPUs
   - Lower memory usage

6. **Image Caching**
   - Cache images in memory
   - Faster data loading
   - Reduces disk I/O bottleneck

## 📈 Monitoring Training

During training, watch these metrics:

### Good Training Signs ✅
- Loss decreasing steadily
- mAP increasing over epochs
- Validation metrics improving
- No huge gap between train/val metrics

### Warning Signs ⚠️
- Loss not decreasing after many epochs
- Validation metrics much worse than training (overfitting)
- Loss oscillating wildly (learning rate too high)
- GPU memory errors (batch size too large)

## 🎛️ Custom Training Parameters

You can modify `train_model.py` to experiment:

### Increase Accuracy (if you have GPU memory):
```python
model = YOLO('yolov8l.pt')  # Use larger model
batch=32,                   # Increase batch size
imgsz=1280,                # Increase image size
```

### Decrease Memory Usage:
```python
batch=8,                    # Reduce batch size
imgsz=640,                 # Reduce image size
cache=False,               # Disable caching
```

### Faster Training (less accuracy):
```python
epochs=100,                # Fewer epochs
patience=30,               # Less patience
close_mosaic=5,           # Close mosaic earlier
```

## 💾 After Training

### Check Your Results

Training outputs are saved to: `runs/detect/yellowcert_model/`

Important files:
- `weights/best.pt` - Best model checkpoint
- `weights/last.pt` - Last epoch checkpoint
- `results.png` - Training metrics plot
- `confusion_matrix.png` - Class confusion
- `val_batch*_pred.jpg` - Validation predictions
- `F1_curve.png` - F1 score curve
- `PR_curve.png` - Precision-Recall curve

### Use Your Model

The best model is automatically copied to `models/best.pt`

To use it:
1. Ensure `models/best.pt` exists
2. Restart your backend: `cd backend && python main.py`
3. Upload an image in the frontend

### Compare Models

If you trained multiple models:
```bash
# Compare metrics
python -c "
from ultralytics import YOLO

model_m = YOLO('models/best.pt')  # YOLOv8m
model_x = YOLO('models/best_max.pt')  # YOLOv8x (if trained)

print('YOLOv8m:', model_m.val())
print('YOLOv8x:', model_x.val())
"
```

## 🐛 Troubleshooting

### Out of Memory Error
```
RuntimeError: CUDA out of memory
```
**Solution:** Reduce `batch` size or `imgsz` in the training script

### Model Not Found
```
Model not found at models/best.pt
```
**Solution:** Run training first: `python train_model.py`

### Low Accuracy
- Check if your dataset has good annotations
- Increase epochs
- Try data augmentation parameters
- Use larger model (YOLOv8l/x)
- Check for class imbalance

### Training Too Slow
- Reduce `imgsz` to 640
- Reduce `batch` size
- Use smaller model (YOLOv8s)
- Check if GPU is being used
- Close other GPU applications

## 📚 Additional Resources

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Training Tips](https://docs.ultralytics.com/modes/train/)
- [Hyperparameter Tuning](https://docs.ultralytics.com/usage/hyperparameter-tuning/)

## 🎯 Recommended Workflow

1. **Start with quick test:**
   ```bash
   python train_quick.py
   ```
   Verify the pipeline works

2. **Train production model:**
   ```bash
   python train_model.py
   ```
   Get your best balanced model

3. **Optional - Maximum accuracy:**
   ```bash
   python train_max_accuracy.py
   ```
   Only if you need absolute best results and have powerful GPU

4. **Evaluate and deploy:**
   - Check metrics in `runs/detect/`
   - Test on new images
   - Deploy `models/best.pt`

---

**Happy Training! 🚀**
