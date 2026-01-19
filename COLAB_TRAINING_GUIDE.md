# 🚀 Google Colab Training Guide for YellowCert

Your M4 Pro Mac is great, but Google Colab's free GPU is better for training! This guide shows you how to train your model on Colab's free T4 GPU.

## 📋 Prerequisites

1. Google account (for Colab)
2. Your YellowCert dataset (train/, valid/, test/, data.yaml)

---

## 🎯 Quick Start (5 Steps)

### Step 1: Prepare Your Dataset

On your Mac, create a ZIP file of your dataset:

```bash
cd /Users/arnon/Downloads/YellowCert
zip -r yellowcert_dataset.zip train/ valid/ test/ data.yaml
```

This creates `yellowcert_dataset.zip` (~size depends on your dataset)

### Step 2: Upload Notebook to Colab

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Upload notebook**
3. Upload `YellowCert_Training_Colab.ipynb` from your YellowCert folder

### Step 3: Enable GPU

**IMPORTANT:** Colab uses CPU by default!

1. Click **Runtime → Change runtime type**
2. Set **Hardware accelerator** to **T4 GPU**
3. Click **Save**

![GPU Selection](https://i.imgur.com/example.png)

### Step 4: Run the Notebook

Execute cells in order:

1. **Section 1**: Setup (installs packages)
2. **Section 2**: Upload your `yellowcert_dataset.zip`
3. **Section 3**: Verify dataset structure
4. **Section 4**: Choose training mode (keep 'balanced')
5. **Section 5**: Start training! ☕ Go grab coffee
6. **Section 8**: Download trained model

### Step 5: Use the Model

After downloading `best.pt`:

```bash
# On your Mac
cd /Users/arnon/Downloads/YellowCert
mv ~/Downloads/best.pt models/best.pt

# Restart backend
cd backend
python main.py
```

---

## 🎛️ Training Modes Comparison

| Mode | Model | Time (T4 GPU) | Accuracy | When to Use |
|------|-------|---------------|----------|-------------|
| **Quick** | YOLOv8n | 15-20 min | ⭐⭐ | Testing pipeline |
| **Balanced** ✅ | YOLOv8m | 2-4 hours | ⭐⭐⭐⭐ | **Recommended** |
| **Maximum** | YOLOv8l | 5-8 hours | ⭐⭐⭐⭐⭐ | Best results |
| **Ultra** | YOLOv8x | 8-12 hours | ⭐⭐⭐⭐⭐ | Absolute maximum |

### Which Mode Should I Choose?

**For most users: BALANCED mode** ✅
- Best accuracy/speed tradeoff
- Fits in free Colab session (~12 hours)
- mAP50: 0.85-0.95

---

## 💾 Two Ways to Upload Dataset

### Method A: Direct Upload (Easier, but slower)

Run this cell in the notebook:
```python
uploaded = files.upload()  # Click and upload yellowcert_dataset.zip
```

**Pros:** Simple, no Google Drive needed
**Cons:** Slower for large datasets, must re-upload if session disconnects

### Method B: Google Drive (Recommended for large datasets)

1. Upload `yellowcert_dataset.zip` to your Google Drive
2. Run the Google Drive cell in notebook
3. Update path: `/content/drive/MyDrive/yellowcert_dataset.zip`

**Pros:** Faster, persistent, reusable
**Cons:** Requires Google Drive setup

---

## 📊 Monitoring Training

### What to Watch:

While training, you'll see:
```
Epoch    GPU_mem   box_loss   cls_loss   dfl_loss   Instances   Size
1/200      8.5G      1.234      0.567      1.890        125      1024
```

**Good signs:** ✅
- Losses decreasing
- mAP increasing each validation
- GPU memory stable (~8-12GB)

**Warning signs:** ⚠️
- Loss stuck or increasing → Stop and restart
- "CUDA out of memory" → Reduce batch size
- Session timeout → Save to Google Drive!

### View Real-Time Progress:

Click the **Files** icon (📁) on left sidebar → `runs/detect/yellowcert_balanced/`

You can download intermediate results anytime!

---

## ⏱️ Session Management

### Colab Free Tier Limits:
- **Session length:** ~12 hours max
- **Idle timeout:** 90 minutes of inactivity
- **Daily limit:** ~12 hours of GPU time

### Tips to Avoid Disconnection:

1. **Keep tab active** (don't close browser)
2. **Save to Google Drive periodically:**
   ```python
   # Add this after training starts (Section 5)
   import shutil
   shutil.copy('/content/runs/detect/yellowcert_balanced/weights/best.pt',
               '/content/drive/MyDrive/yellowcert_checkpoint.pt')
   ```
3. **Use Colab Pro** ($10/month) for:
   - Longer sessions
   - Better GPUs (A100)
   - Background execution

### If Session Disconnects:

Don't panic! Your work is saved in Google Drive (if you used Method B).

To resume:
1. Reconnect to runtime
2. Re-run setup cells
3. Training will resume from last checkpoint (if configured)

---

## 🎁 What You'll Get

After training completes:

### Files Downloaded:

1. **`best.pt`** (~50-130 MB depending on model)
   - Your trained model weights
   - Ready to use in your app!

2. **`yellowcert_results.zip`** (Optional, ~100-500 MB)
   - All training plots
   - Confusion matrix
   - Validation predictions
   - Training logs
   - Last checkpoint

### Training Visualizations:

- `results.png` - Training curves (loss, mAP, precision, recall)
- `confusion_matrix.png` - Per-class accuracy
- `F1_curve.png` - F1 scores
- `PR_curve.png` - Precision-Recall curves
- `val_batch*_pred.jpg` - Sample predictions

---

## 🐛 Troubleshooting

### "No GPU detected"
**Problem:** Notebook is using CPU
**Solution:** Runtime → Change runtime type → GPU (T4)

### "CUDA out of memory"
**Problem:** Batch size too large for GPU
**Solution:** In Section 4, edit config:
```python
'batch': 8,  # Reduce from 16 to 8
```

### "Session disconnected"
**Problem:** Colab timeout or connection loss
**Solution:**
1. Save to Google Drive regularly
2. Keep browser tab active
3. Consider Colab Pro

### "Dataset not found"
**Problem:** Upload failed or wrong path
**Solution:**
```python
# Verify dataset location
!ls -la /content/yellowcert
!cat /content/yellowcert/data.yaml
```

### Training too slow
**Problem:** Using CPU instead of GPU
**Solution:** Check GPU is enabled (Step 3)

### Low accuracy after training
**Problem:** Dataset issues or insufficient training
**Solutions:**
1. Train longer (increase epochs)
2. Check dataset annotations
3. Try larger model (Maximum/Ultra mode)

---

## 💡 Pro Tips

### 1. Start Small, Scale Up
```
Run 1: Quick mode (10 epochs) → Verify everything works
Run 2: Balanced mode (200 epochs) → Production model
Run 3: Maximum mode (300 epochs) → If you need better accuracy
```

### 2. Save Intermediate Checkpoints
The notebook auto-saves every 10 epochs to:
```
runs/detect/yellowcert_balanced/weights/
├── best.pt      # Best mAP model
├── last.pt      # Most recent
├── epoch10.pt   # Checkpoint at epoch 10
└── epoch20.pt   # etc.
```

### 3. Compare Multiple Runs
Train with different settings and compare:
```python
from ultralytics import YOLO

model1 = YOLO('run1_best.pt')
model2 = YOLO('run2_best.pt')

print("Model 1:", model1.val())
print("Model 2:", model2.val())
```

### 4. Test Before Downloading
Use Section 9 (Test on Sample Image) to verify model works before downloading!

### 5. Batch Process Multiple Experiments
Want to try different settings? Run multiple notebooks:
- Notebook 1: YOLOv8m, 200 epochs
- Notebook 2: YOLOv8l, 300 epochs
- Compare results!

---

## 📈 Expected Results

### T4 GPU (Colab Free):

| Mode | Training Time | mAP50 | mAP50-95 | Model Size |
|------|---------------|-------|----------|------------|
| Quick | 15-20 min | 0.70-0.80 | 0.55-0.65 | ~6 MB |
| Balanced | 2-4 hours | **0.85-0.95** | **0.70-0.85** | ~52 MB |
| Maximum | 5-8 hours | 0.90-0.96 | 0.75-0.88 | ~87 MB |
| Ultra | 8-12 hours | 0.92-0.98 | 0.78-0.92 | ~136 MB |

### A100 GPU (Colab Pro):

- **2-3x faster** training
- Can handle larger batch sizes
- Same accuracy, less time!

---

## 🆚 Colab vs M4 Pro Mac

| Feature | M4 Pro Mac | Colab T4 | Colab A100 (Pro) |
|---------|------------|----------|------------------|
| **Cost** | Owned | Free | $10/month |
| **Speed** | Medium | Fast | Very Fast |
| **VRAM** | Shared (~16GB) | 16GB VRAM | 40GB VRAM |
| **Session** | Unlimited | 12 hours | 24 hours |
| **Best for** | Small models | Balanced models | Large models |

**Recommendation:** Use Colab for training, Mac for inference/deployment

---

## 🎯 Complete Workflow Example

### Day 1: Prepare
```bash
# On Mac
cd /Users/arnon/Downloads/YellowCert
zip -r yellowcert_dataset.zip train/ valid/ test/ data.yaml
```

### Day 2: Train on Colab
1. Upload notebook to Colab
2. Enable GPU (T4)
3. Upload dataset ZIP
4. Choose 'balanced' mode
5. Start training (2-4 hours)
6. Download `best.pt`

### Day 3: Deploy on Mac
```bash
# On Mac
mv ~/Downloads/best.pt /Users/arnon/Downloads/YellowCert/models/
cd /Users/arnon/Downloads/YellowCert/backend
python main.py
```

### Day 4: Test & Iterate
1. Test in web app
2. Evaluate results
3. If needed, retrain with 'maximum' mode on Colab

---

## 📚 Additional Resources

- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [YOLOv8 Training Tips](https://docs.ultralytics.com/modes/train/)
- [Colab Pro Benefits](https://colab.research.google.com/signup)

---

## ✅ Checklist

Before starting:
- [ ] Created `yellowcert_dataset.zip`
- [ ] Uploaded notebook to Colab
- [ ] Enabled GPU (T4)
- [ ] Chosen training mode
- [ ] Have 3-4 hours available (for balanced mode)

After training:
- [ ] Downloaded `best.pt`
- [ ] Moved to `models/` folder
- [ ] Restarted backend
- [ ] Tested in web app
- [ ] Checked model accuracy

---

## 🎉 You're Ready!

Open `YellowCert_Training_Colab.ipynb` in Google Colab and start training!

**Questions?** Check the troubleshooting section or open an issue.

**Happy Training!** 🚀🏥
