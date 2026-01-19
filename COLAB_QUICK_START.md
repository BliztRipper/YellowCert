# 🚀 Google Colab Training - Quick Start

Train YellowCert on Google's free GPU in 5 minutes!

## ⚡ Super Quick Start

### Step 1: Prepare Dataset (On Your Mac)
```bash
cd /Users/arnon/Downloads/YellowCert
./prepare_for_colab.sh
```
This creates `yellowcert_dataset.zip`

### Step 2: Open Colab
1. Go to **https://colab.research.google.com/**
2. Click **File → Upload notebook**
3. Upload `YellowCert_Training_Colab.ipynb`

### Step 3: Enable GPU
1. Click **Runtime → Change runtime type**
2. Select **T4 GPU**
3. Click **Save**

### Step 4: Run Training
Execute cells in order:
- ✅ Cell 1: Check GPU
- ✅ Cell 2: Install packages
- ✅ Cell 3: Upload `yellowcert_dataset.zip`
- ✅ Cell 4: Keep default `TRAINING_MODE = 'balanced'`
- ✅ Cell 5: **Start training** (2-4 hours) ☕
- ✅ Cell 8: Download `best.pt`

### Step 5: Use the Model
```bash
# On your Mac
cd /Users/arnon/Downloads/YellowCert
mv ~/Downloads/best.pt models/best.pt

# Restart backend
cd backend
python main.py
```

## 📊 Training Modes

| Mode | Time | Accuracy | Recommended For |
|------|------|----------|-----------------|
| `quick` | 15 min | ⭐⭐ | Testing |
| `balanced` ✅ | 2-4 hrs | ⭐⭐⭐⭐ | **Production** |
| `maximum` | 5-8 hrs | ⭐⭐⭐⭐⭐ | Best quality |
| `ultra` | 8-12 hrs | ⭐⭐⭐⭐⭐ | Maximum |

**Default is `balanced` - perfect for most users!**

## ⚠️ Important Tips

1. **Don't close browser** during training
2. **Save to Google Drive** for long sessions
3. **Free tier = 12 hours max** (enough for balanced mode)
4. **Monitor progress** in Colab output

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "No GPU" | Runtime → Change runtime type → T4 GPU |
| "Out of memory" | **Use `YellowCert_Training_Colab_v2.ipynb`** or see `COLAB_OOM_FIX.md` |
| "Session disconnected" | Save to Google Drive (cell at bottom) |
| "Dataset not found" | Re-upload zip file in cell 3 |

### 🚨 Out of Memory Error?

**Quick fix:** Use the optimized notebook instead:
1. Upload **`YellowCert_Training_Colab_v2.ipynb`** (not the old one)
2. This version is pre-configured for T4 GPU
3. Uses safe batch sizes and image sizes

**Or** see detailed fixes in: `COLAB_OOM_FIX.md`

## 📚 Need More Help?

Read the full guide: **`COLAB_TRAINING_GUIDE.md`**

---

**That's it! Start training in 5 minutes! 🎉**
