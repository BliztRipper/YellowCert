# 🚀 Google Colab Training - README

Got an **Out of Memory error**? You're in the right place!

## ⚡ Quick Fix (Choose One)

### Option 1: Use the Fixed Notebook ✅ **RECOMMENDED**

1. **Upload `YellowCert_Training_Colab_v2.ipynb`** to Colab (not v1)
2. This version is optimized for T4 GPU
3. Follow the cells normally
4. Works perfectly on free Colab!

### Option 2: Fix Your Current Notebook

1. Open your current notebook in Colab
2. Add a new cell **BEFORE** the training cell
3. Copy the contents of `colab_memory_fix.py`
4. Run it, then run training

### Option 3: Manual Fix

In your notebook, change these settings before training:
```python
# Add this cell before training:
config['batch'] = 8        # Reduce batch size
config['imgsz'] = 640      # Reduce image size
config['model'] = 'yolov8s.pt'  # Use smaller model
```

## 📁 File Guide

| File | Purpose | When to Use |
|------|---------|-------------|
| **`YellowCert_Training_Colab_v2.ipynb`** ✅ | Optimized notebook | **Use this for training** |
| `YellowCert_Training_Colab.ipynb` | Original (has OOM issue) | Don't use (kept for reference) |
| `COLAB_OOM_FIX.md` | Detailed OOM solutions | When you get memory errors |
| `COLAB_QUICK_START.md` | 5-minute guide | Quick reference |
| `COLAB_TRAINING_GUIDE.md` | Complete guide | Detailed instructions |
| `colab_memory_fix.py` | Memory fix code | To fix existing notebook |
| `prepare_for_colab.sh` | Dataset preparation | Run on Mac before Colab |

## 🎯 Recommended Workflow

### For Your M4 Pro:

```bash
# Step 1: Prepare dataset on Mac
cd /Users/arnon/Downloads/YellowCert
./prepare_for_colab.sh
# Creates: yellowcert_dataset.zip
```

### On Google Colab:

1. Go to https://colab.research.google.com/
2. Upload **`YellowCert_Training_Colab_v2.ipynb`**
3. Runtime → Change runtime type → **T4 GPU**
4. Run cells 1-4 (setup and upload)
5. Cell 5: Keep `TRAINING_MODE = 'balanced'`
6. Run training (2-3 hours)
7. Download `best.pt`

### Back on Mac:

```bash
# Step 2: Use the trained model
cd /Users/arnon/Downloads/YellowCert
mv ~/Downloads/best.pt models/best.pt

# Step 3: Start backend
cd backend
python main.py

# Step 4: Test in browser at http://localhost:3000
```

## 📊 Which Training Mode?

For **T4 GPU (Colab Free)**:

| Mode | Model | Time | mAP50 | Recommended |
|------|-------|------|-------|-------------|
| `quick` | YOLOv8n | 15 min | 0.70-0.80 | Testing only |
| `balanced` ✅ | YOLOv8s | 2-3 hrs | **0.80-0.90** | **Yes!** |
| `advanced` | YOLOv8m | 3-4 hrs | 0.85-0.93 | If time allows |
| `maximum` | YOLOv8m | 4-5 hrs | 0.87-0.95 | Max for T4 |

**Start with `balanced`** - best results for the time!

## 🆘 Common Issues

### "Out of Memory"
→ Use `YellowCert_Training_Colab_v2.ipynb`
→ Or see `COLAB_OOM_FIX.md`

### "No GPU detected"
→ Runtime → Change runtime type → T4 GPU

### "Session disconnected"
→ Save to Google Drive (run cell 10)
→ Keep browser tab open

### "Low accuracy"
→ Use `advanced` or `maximum` mode
→ Train longer (more epochs)

## 📈 What to Expect

### Balanced Mode (Recommended):
- **Training time:** 2-3 hours
- **mAP50:** 0.80-0.90 (80-90% accuracy)
- **Model size:** ~25 MB
- **Inference speed:** Fast
- **Quality:** Excellent for production ✅

### Advanced Mode:
- **Training time:** 3-4 hours
- **mAP50:** 0.85-0.93
- **Model size:** ~50 MB
- **Inference speed:** Medium
- **Quality:** Better than balanced

## 💡 Pro Tips

1. **Always use v2 notebook** - It's optimized for T4
2. **Start with balanced mode** - Don't jump to maximum
3. **Save to Google Drive** - After training completes
4. **Test before downloading** - Use the test cell (#9)
5. **Keep browser open** - Prevents timeout

## 🔗 Quick Links

- **Colab:** https://colab.research.google.com/
- **Issue?** See `COLAB_OOM_FIX.md`
- **Guide:** See `COLAB_TRAINING_GUIDE.md`
- **Quick start:** See `COLAB_QUICK_START.md`

## ✅ Success Checklist

Before starting:
- [ ] Ran `./prepare_for_colab.sh` on Mac
- [ ] Have `yellowcert_dataset.zip` ready
- [ ] Using **v2 notebook** (not v1)
- [ ] Enabled GPU in Colab (T4)
- [ ] Chose `balanced` mode

After training:
- [ ] Downloaded `best.pt`
- [ ] Saved to Google Drive (backup)
- [ ] Moved to `models/` folder
- [ ] Restarted backend
- [ ] Tested in web app

---

**Need help?** Read the detailed guides or open an issue.

**Ready to train?** Use `YellowCert_Training_Colab_v2.ipynb` ✅
