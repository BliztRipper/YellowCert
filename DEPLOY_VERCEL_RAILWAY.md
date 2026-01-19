# 🚀 Deploy YellowCert: Vercel + Railway

Complete guide to deploy your YellowCert app professionally!

**Frontend:** Vercel (Free, Fast CDN)
**Backend:** Railway ($5/month, ML-optimized)

**Total Setup Time:** ~30 minutes
**Total Cost:** $0 (trial) then $5/month

---

## 📋 Prerequisites

- [ ] GitHub account
- [ ] Trained model (`models/best.pt` exists)
- [ ] Project pushed to GitHub

---

## Part 1: Deploy Backend to Railway 🚂

### Step 1: Prepare Your Project

First, let's create the necessary configuration files:

```bash
cd /Users/arnon/Downloads/YellowCert
```

The configuration files will be created automatically in the next steps.

### Step 2: Push to GitHub

```bash
# Initialize git if not already done
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Step 3: Sign Up for Railway

1. Go to https://railway.app/
2. Click **"Start a New Project"**
3. Sign in with GitHub
4. Authorize Railway to access your repos

### Step 4: Deploy Backend

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your **YellowCert** repository
4. Railway will detect it as a Python app

### Step 5: Configure Environment

1. In Railway dashboard, click your service
2. Go to **"Variables"** tab
3. Add these variables:
   ```
   PORT=8000
   PYTHONUNBUFFERED=1
   ```

### Step 6: Upload Model File

⚠️ **Important:** Railway has file size limits in Git, so we'll upload the model separately:

**Option A: Use Railway Volume (Recommended)**

1. In Railway, go to **"Settings"** → **"Volumes"**
2. Create new volume: `/app/models`
3. Upload `best.pt` to the volume

**Option B: Use External Storage**

Upload to cloud storage and download on startup:
```python
# In backend/main.py startup, add:
import requests
import os

@app.on_event("startup")
async def download_model():
    if not os.path.exists(MODEL_PATH):
        # Download from cloud storage
        url = "YOUR_MODEL_URL"  # Upload to Dropbox/Google Drive
        response = requests.get(url)
        with open(MODEL_PATH, 'wb') as f:
            f.write(response.content)
```

### Step 7: Get Backend URL

1. Once deployed, Railway will show you a URL like:
   ```
   https://yellowcert-backend-production.up.railway.app
   ```
2. **Copy this URL** - you'll need it for frontend!

3. Test it:
   ```bash
   curl https://your-railway-url.railway.app/
   ```
   Should return: `{"message":"YellowCert Detection API","status":"running"}`

---

## Part 2: Deploy Frontend to Vercel 🎨

### Step 1: Update Frontend Configuration

Update the API URL in your frontend:

```bash
cd /Users/arnon/Downloads/YellowCert/frontend
```

Edit `src/App.js`:
```javascript
// Change this line:
const API_URL = 'http://localhost:8000';

// To use environment variable:
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
```

Commit the change:
```bash
git add src/App.js
git commit -m "Use environment variable for API URL"
git push
```

### Step 2: Sign Up for Vercel

1. Go to https://vercel.com/
2. Click **"Sign Up"**
3. Sign in with GitHub
4. Authorize Vercel

### Step 3: Deploy Frontend

1. Click **"Add New Project"**
2. Import your **YellowCert** repository
3. Configure:
   - **Framework Preset:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `build`

### Step 4: Add Environment Variable

1. In deployment settings, go to **"Environment Variables"**
2. Add:
   ```
   Name: REACT_APP_API_URL
   Value: https://your-railway-url.railway.app
   ```
   (Use your Railway URL from Part 1, Step 7)

3. Click **"Deploy"**

### Step 5: Get Frontend URL

Vercel will give you a URL like:
```
https://yellowcert-frontend.vercel.app
```

---

## Part 3: Configure CORS 🔐

Update backend CORS to allow your Vercel domain:

Edit `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://yellowcert-frontend.vercel.app",  # Add your Vercel URL
        "https://*.vercel.app"  # Allow all Vercel preview deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Commit and push:
```bash
git add backend/main.py
git commit -m "Update CORS for production"
git push
```

Railway will auto-redeploy!

---

## Part 4: Test Your Deployment 🧪

1. Open your Vercel URL: `https://yellowcert-frontend.vercel.app`
2. Upload a vaccination certificate image
3. Click **"Analyze Certificate"**
4. Should see detections! 🎉

---

## 📊 Deployment Summary

| Service | Platform | URL | Cost |
|---------|----------|-----|------|
| Frontend | Vercel | `https://yellowcert-frontend.vercel.app` | Free |
| Backend | Railway | `https://yellowcert-backend.railway.app` | $5/mo* |
| **Total** | - | - | **$5/mo** |

*Railway offers $5 free trial credit

---

## 🎯 Custom Domain (Optional)

### For Frontend (Vercel):

1. Go to Vercel project settings
2. Click **"Domains"**
3. Add your domain: `yellowcert.com`
4. Follow DNS setup instructions

### For Backend (Railway):

1. Go to Railway project settings
2. Click **"Settings"** → **"Domains"**
3. Add custom domain: `api.yellowcert.com`
4. Update DNS with CNAME record

---

## 🔧 Troubleshooting

### Frontend can't connect to backend

**Check:**
1. ✅ CORS is configured correctly
2. ✅ REACT_APP_API_URL is set
3. ✅ Railway backend is running
4. ✅ No typos in URLs

**Fix:**
```bash
# Rebuild frontend with correct API URL
# In Vercel dashboard:
# 1. Go to project settings
# 2. Environment Variables → Edit REACT_APP_API_URL
# 3. Deployments → Redeploy
```

### Model not found error

**Check:**
1. ✅ `models/best.pt` exists
2. ✅ Model uploaded to Railway volume
3. ✅ Path is correct in `main.py`

**Fix:**
- Upload model to Railway volume
- Or use cloud storage URL method

### Railway deployment fails

**Common causes:**
- Missing `requirements.txt`
- Wrong Python version
- Missing Procfile

**Fix:**
See configuration files section below

---

## 📁 Required Configuration Files

### 1. `backend/requirements.txt`

Make sure it includes:
```txt
fastapi
uvicorn[standard]
ultralytics
opencv-python-headless
pillow
python-multipart
numpy
```

### 2. `Procfile` (in root directory)

```
web: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

### 3. `runtime.txt` (optional, in root)

```
python-3.11.0
```

### 4. `.gitignore`

Make sure to exclude:
```
models/best.pt
node_modules/
__pycache__/
*.pyc
.env
```

---

## 🔄 Continuous Deployment

Both platforms support auto-deployment:

**Vercel:**
- Push to `main` → Auto-deploys frontend ✅

**Railway:**
- Push to `main` → Auto-deploys backend ✅

**Workflow:**
```bash
# Make changes
git add .
git commit -m "Update feature"
git push

# Both frontend and backend deploy automatically!
```

---

## 💰 Cost Breakdown

### Free Tier Limits:

**Vercel (Free Forever):**
- ✅ 100 GB bandwidth/month
- ✅ Unlimited sites
- ✅ Auto SSL
- ✅ Global CDN

**Railway (After $5 trial):**
- 💵 $5/month base
- 💵 +$0.000231/GB transferred
- 💵 +$0.00463/hour compute

**Estimated monthly cost:** $5-10 depending on usage

**Tips to save:**
- Use Railway free trial ($5 credit)
- Optimize Docker image size
- Use caching
- Consider Render free tier (alternative)

---

## 🎉 You're Live!

Your YellowCert app is now:
- ✅ Deployed globally
- ✅ Auto-updating from Git
- ✅ Production-ready
- ✅ Scalable
- ✅ Professional URLs

Share your app:
```
🌐 https://yellowcert-frontend.vercel.app
```

---

## 📚 Next Steps

1. **Add custom domain** for professional look
2. **Monitor usage** in Railway/Vercel dashboards
3. **Set up analytics** (Google Analytics, Vercel Analytics)
4. **Add authentication** if needed
5. **Optimize performance** based on usage

---

## 🆘 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Railway Docs:** https://docs.railway.app/
- **Issues:** Check `DEPLOYMENT_ANALYSIS.md`

**Quick Links:**
- Frontend: https://vercel.com/dashboard
- Backend: https://railway.app/dashboard

---

**Congratulations! Your YellowCert app is live! 🎉**
