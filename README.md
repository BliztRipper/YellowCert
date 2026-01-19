# 🏥 YellowCert - Medical Certificate Detection

AI-powered vaccination certificate detection using YOLOv8 object detection with a professional medical-themed UI.

![Status](https://img.shields.io/badge/status-deployed-success)
![Frontend](https://img.shields.io/badge/frontend-Vercel-black)
![Backend](https://img.shields.io/badge/backend-Render-46E3B7)

**Live Demo:** https://yellow-cert.vercel.app

---

## ✨ Features

- 🤖 **YOLOv8 Object Detection** - Detects 8 different elements on vaccination certificates
- 🎨 **Modern Medical UI** - React-based frontend with professional medical theme
- 📊 **Visual Results** - Bounding boxes with confidence scores
- ⚡ **Fast API Backend** - Python FastAPI server for ML inference
- 🎯 **High Accuracy** - Trained on specialized vaccination certificate dataset
- 🚀 **Production Ready** - Deployed and optimized for real-world use

---

## 🔍 Detected Classes

The model can detect these elements on vaccination certificates:

| Class | Icon | Description |
|-------|------|-------------|
| **Cholera** | 💉 | Cholera vaccination info |
| **COVID-19** | 🦠 | COVID-19 vaccination details |
| **Date** | 📅 | Date stamps |
| **Flu** | 🤧 | Influenza vaccination |
| **Logo** | 🏥 | Official logos and stamps |
| **Meningococcal** | 🧬 | Meningococcal vaccine |
| **Signature** | ✍️ | Doctor signatures |
| **Yellow Fever** | 🌍 | Yellow fever vaccination |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git

### Local Development

```bash
# 1. Clone the repository
git clone https://github.com/BliztRipper/YellowCert.git
cd YellowCert

# 2. Set up backend
cd backend
pip install -r requirements.txt
python main.py
# Backend runs at http://localhost:8000

# 3. Set up frontend (new terminal)
cd frontend
npm install
npm start
# Frontend runs at http://localhost:3000
```

### Quick Scripts

```bash
# Backend
./start_backend.sh

# Frontend
./start_frontend.sh

# Setup environment
./setup_env.sh
```

---

## 🎓 Training

Train your own model with our optimized training scripts:

### Local Training (Mac/PC)

```bash
python train_model.py
```

**Features:**
- YOLOv8m model for balanced accuracy/speed
- 200 epochs with early stopping
- AdamW optimizer
- Comprehensive data augmentation

### Google Colab Training (Recommended)

Free GPU training on Google Colab:

```bash
# 1. Prepare dataset
./prepare_for_colab.sh

# 2. Upload YellowCert_Training_Colab_v2.ipynb to Colab
# 3. Follow the notebook instructions
```

**📖 Training Guides:**
- **Quick Start:** `COLAB_QUICK_START.md`
- **Complete Guide:** `COLAB_TRAINING_GUIDE.md`

**Training Options:**
| Mode | Model | Time (T4 GPU) | mAP50 |
|------|-------|---------------|-------|
| Quick | YOLOv8n | 15-20 min | 0.70-0.80 |
| **Balanced** ✅ | YOLOv8s | 2-3 hrs | **0.80-0.90** |
| Advanced | YOLOv8m | 3-4 hrs | 0.85-0.93 |
| Maximum | YOLOv8m | 4-5 hrs | 0.87-0.95 |

---

## 🌐 Deployment

Deploy your app to production in minutes:

### Option 1: Free Deployment (Vercel + Render)

**Cost:** $0/month | **Tradeoff:** 30-60s cold starts

**Frontend (Vercel):**
- Auto-deploys from Git
- Global CDN
- Free SSL

**Backend (Render Free):**
- 750 hours/month free
- Cold starts after 15min inactivity

📖 **Guide:** `DEPLOY_VERCEL_RENDER.md`

### Option 2: Production Deployment (Vercel + Railway)

**Cost:** $5/month | **Benefit:** No cold starts

**Frontend (Vercel):**
- Same as above

**Backend (Railway):**
- Always on
- Fast response
- Better for production

📖 **Guide:** `DEPLOY_VERCEL_RAILWAY.md`

### Quick Decision

**Start here:** `DEPLOYMENT_QUICK_START.md`

---

## 📁 Project Structure

```
YellowCert/
├── backend/
│   ├── main.py              # FastAPI server
│   └── .env.example         # Environment template
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── App.css          # Medical theme styles
│   │   └── index.js         # Entry point
│   ├── public/
│   └── package.json
├── models/
│   └── best.pt             # Trained YOLOv8 model
├── train/                  # Training dataset
├── valid/                  # Validation dataset
├── test/                   # Test dataset
├── train_model.py          # Training script
├── data.yaml              # Dataset configuration
└── requirements.txt       # Python dependencies
```

---

## 🎨 Medical Theme UI

Professional medical-themed interface with:

- ✅ Teal/cyan color palette
- ✅ Clean, modern design
- ✅ High-contrast element colors
- ✅ Responsive layout
- ✅ Smooth animations

**Customization:** See `COLOR_PALETTE.md`

---

## 🔧 API Endpoints

### GET `/`
Health check

**Response:**
```json
{
  "message": "YellowCert Detection API",
  "status": "running"
}
```

### POST `/predict`
Upload image for detection

**Request:**
```bash
curl -X POST -F "file=@certificate.jpg" http://localhost:8000/predict
```

**Response:**
```json
{
  "success": true,
  "detections": [
    {
      "class": "yellowfever",
      "confidence": 0.88,
      "bbox": {
        "x1": 100,
        "y1": 200,
        "x2": 300,
        "y2": 400
      }
    }
  ],
  "image_size": {
    "width": 1034,
    "height": 690
  }
}
```

---

## 🛠️ Technologies

### Backend
- **FastAPI** - Modern Python web framework
- **Ultralytics YOLOv8** - State-of-the-art object detection
- **OpenCV** - Image processing
- **PyTorch** - Deep learning framework

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **Canvas API** - Bounding box visualization

### Deployment
- **Vercel** - Frontend hosting
- **Railway/Render** - Backend hosting
- **Google Colab** - Model training

---

## 📊 Model Performance

Trained on YellowCert dataset with optimized parameters:

- **Model:** YOLOv8m (balanced)
- **mAP50:** 0.85-0.95
- **mAP50-95:** 0.70-0.85
- **Inference:** ~2-3 seconds per image
- **Classes:** 8 detected elements

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

---

## 📝 License

This project uses the YellowCert dataset which is licensed under CC BY 4.0.

---

## 📚 Documentation

- 📖 **Deployment:** `DEPLOYMENT_QUICK_START.md`
- 🎓 **Training:** `COLAB_TRAINING_GUIDE.md`
- 🎨 **UI Customization:** `COLOR_PALETTE.md`
- ⚙️ **Project Settings:** `CLAUDE.md`

---

## 🔗 Links

- **Live Demo:** https://yellow-cert.vercel.app
- **Dataset:** [YellowCert on Roboflow](https://universe.roboflow.com/vitchakorn/yellowcert)
- **YOLOv8:** [Ultralytics](https://github.com/ultralytics/ultralytics)

---

## ⭐ Show Your Support

If this project helped you, please consider giving it a star!

---

**Built with ❤️ for medical certificate detection**
