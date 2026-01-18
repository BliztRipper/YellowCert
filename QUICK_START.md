# YellowCert - Quick Start Guide

## ✅ Environment Created!

Your conda environment `yellowcert` with Python 3.12 has been created successfully.

## 📦 Installation Steps

Run this command to install all Python dependencies:

```bash
./install_deps.sh
```

This will:
- Activate the `yellowcert` conda environment
- Install FastAPI, Ultralytics YOLO, PyTorch, and other dependencies
- Take ~5-10 minutes (downloading PyTorch is large)

**OR** install manually:

```bash
conda activate yellowcert
pip install -r requirements.txt
```

## 🚀 Running the Application

### Step 1: Train the Model (First Time Only)

```bash
conda activate yellowcert
python train_model.py
```

This will:
- Train YOLOv8 on your vaccination certificate dataset
- Save the best model to `models/best.pt`
- Take 30-60 minutes depending on your hardware (GPU recommended)

### Step 2: Start Backend Server

```bash
./start_backend.sh
```

The API will be available at: `http://localhost:8000`

### Step 3: Start Frontend (New Terminal)

```bash
cd frontend
npm install
npm start
```

The web app will open at: `http://localhost:3000`

## 🎯 Usage

1. Open `http://localhost:3000` in your browser
2. Click "Choose Image" and select a vaccination certificate
3. Click "Detect" to run the model
4. View results with bounding boxes and confidence scores

## 📝 Quick Commands

| Task | Command |
|------|---------|
| Activate environment | `conda activate yellowcert` |
| Install dependencies | `./install_deps.sh` |
| Train model | `python train_model.py` |
| Start backend | `./start_backend.sh` |
| Start frontend | `cd frontend && npm start` |
| Deactivate environment | `conda deactivate` |

## 🐛 Troubleshooting

### "conda: command not found"
```bash
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh
```

### "Model not found" error
Make sure you've trained the model first:
```bash
python train_model.py
```

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check `http://localhost:8000` in browser
- Verify no firewall blocking the connection

## 📚 Full Documentation

See `README_APP.md` for complete documentation including:
- Detailed architecture
- API endpoints
- Customization options
- Advanced configuration
