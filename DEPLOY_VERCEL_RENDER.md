# 🚀 Deploy YellowCert: Vercel + Render (FREE)

Complete guide to deploy your YellowCert app for **FREE**!

**Frontend:** Vercel (Free)
**Backend:** Render (Free tier)

**Total Cost:** $0/month ✅

⚠️ **Note:** Render free tier has cold starts (30-60 seconds for first request after inactivity)

---

## 📋 Prerequisites

- [ ] GitHub account
- [ ] Trained model (`models/best.pt`)
- [ ] Project pushed to GitHub

---

## Part 1: Deploy Backend to Render 🎨

### Step 1: Sign Up for Render

1. Go to https://render.com/
2. Click **"Get Started"**
3. Sign up with GitHub
4. Authorize Render

### Step 2: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your **YellowCert** repository
3. Configure:
   - **Name:** `yellowcert-backend`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** `.` (leave empty or use `.`)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Configure Environment Variables

In the environment variables section, add:

```
PORT=8000
PYTHONUNBUFFERED=1
FRONTEND_URL=https://your-app.vercel.app
```

(You'll update FRONTEND_URL later after deploying frontend)

### Step 4: Choose Free Plan

1. Scroll down to **"Plans"**
2. Select **"Free"** plan
   - 750 hours/month free
   - Spins down after 15 min inactivity
   - Cold start: 30-60 seconds

3. Click **"Create Web Service"**

### Step 5: Upload Model File

⚠️ **Important:** Large files can't be in Git

**Option A: Use External Storage (Recommended)**

1. Upload `best.pt` to Dropbox/Google Drive
2. Get a direct download link
3. Update `backend/main.py`:

```python
import requests
import os

@app.on_event("startup")
async def load_model():
    global model
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "best.pt")

    # Download model if not exists
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

        # Replace with your model URL
        model_url = os.getenv("MODEL_URL", "YOUR_DROPBOX_DIRECT_LINK")

        response = requests.get(model_url)
        with open(MODEL_PATH, 'wb') as f:
            f.write(response.content)
        print("Model downloaded successfully!")

    model = YOLO(MODEL_PATH)
    print(f"Model loaded from {MODEL_PATH}")
```

4. Add environment variable in Render:
   ```
   MODEL_URL=https://your-direct-download-link
   ```

**Option B: Use Render Disk (Paid)**

Render Disk costs $0.25/GB/month - not ideal for free tier.

### Step 6: Wait for Deployment

1. Render will build and deploy (takes 5-10 minutes)
2. Once "Live", you'll get a URL:
   ```
   https://yellowcert-backend.onrender.com
   ```
3. **Copy this URL!**

4. Test it:
   ```bash
   curl https://yellowcert-backend.onrender.com/
   ```
   Should return: `{"message":"YellowCert Detection API","status":"running"}`

---

## Part 2: Deploy Frontend to Vercel 🎨

### Step 1: Sign Up for Vercel

1. Go to https://vercel.com/
2. Sign in with GitHub
3. Authorize Vercel

### Step 2: Import Project

1. Click **"Add New Project"**
2. Import **YellowCert** repository
3. Configure:
   - **Framework Preset:** Create React App
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build` (auto-detected)
   - **Output Directory:** `build` (auto-detected)

### Step 3: Add Environment Variable

In **"Environment Variables"** section:

```
Name: REACT_APP_API_URL
Value: https://yellowcert-backend.onrender.com
```

(Use your Render URL from Part 1, Step 6)

Click **"Deploy"**!

### Step 4: Get Frontend URL

Vercel will deploy and give you:
```
https://yellowcert.vercel.app
```

**Copy this URL!**

---

## Part 3: Update Backend CORS 🔐

Now update backend with frontend URL:

1. Go back to **Render dashboard**
2. Click your **yellowcert-backend** service
3. Go to **"Environment"**
4. Update `FRONTEND_URL`:
   ```
   FRONTEND_URL=https://yellowcert.vercel.app
   ```
5. Save changes
6. Render will auto-redeploy

---

## Part 4: Test Your Free Deployment 🧪

1. Open: `https://yellowcert.vercel.app`
2. Upload a vaccination certificate
3. Click **"Analyze Certificate"**
4. ⏳ **First request:** Wait 30-60 seconds (cold start)
5. ✅ **See detections!**

**Subsequent requests:** Fast! (~1-3 seconds)

---

## 📊 Free Tier Comparison

| Service | Platform | Cost | Limits |
|---------|----------|------|--------|
| Frontend | Vercel | Free ✅ | 100 GB bandwidth/month |
| Backend | Render | Free ✅ | 750 hours/month, cold starts |
| **Total** | - | **$0/month** | ⚠️ Cold starts on Render |

---

## ⚠️ Free Tier Limitations

### Render Free Tier:

**Pros:**
- ✅ Completely free
- ✅ 750 hours/month (enough for most apps)
- ✅ Decent performance when warm

**Cons:**
- ❌ **Cold starts:** 30-60 seconds after 15 min inactivity
- ❌ Spins down when not in use
- ❌ Slower than paid tiers
- ❌ No custom domains (on free tier)

**Cold Start Explained:**
- App inactive for 15 minutes → Render shuts it down
- Next request → Render starts it up (30-60 seconds)
- App stays warm while in use

**Mitigation:**
1. Use a free uptime monitor (UptimeRobot) to ping every 10 minutes
2. Upgrade to Render paid tier ($7/month) for no cold starts
3. Accept cold starts for low-traffic apps

### Vercel Free Tier:

**Pros:**
- ✅ No cold starts
- ✅ Fast global CDN
- ✅ 100 GB bandwidth
- ✅ Custom domains

**Cons:**
- ⚠️ 100 GB bandwidth limit (usually enough)

---

## 🎯 Keep Your App Warm (Optional)

To avoid cold starts on Render free tier:

### Method 1: UptimeRobot (Free)

1. Go to https://uptimerobot.com/
2. Sign up free
3. Create new monitor:
   - **Type:** HTTP(s)
   - **URL:** `https://yellowcert-backend.onrender.com/`
   - **Interval:** 5 minutes
4. Save

Now your backend will be pinged every 5 minutes, staying warm!

### Method 2: Upgrade to Render Paid

$7/month for:
- ✅ No cold starts
- ✅ Always running
- ✅ Better performance
- ✅ More hours

---

## 🔄 Continuous Deployment

Both platforms auto-deploy:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push

# Auto-deploys! 🚀
# Vercel: Instant
# Render: 5-10 minutes
```

---

## 🔧 Troubleshooting

### "502 Bad Gateway" on first request

**Cause:** Cold start in progress
**Fix:** Wait 30-60 seconds and refresh

### Frontend can't connect to backend

**Check:**
1. Render service is "Live" (green dot)
2. CORS configured correctly
3. REACT_APP_API_URL is correct
4. Environment variables saved

### Model file not found

**Check:**
1. MODEL_URL is set correctly
2. Download link is direct (not a web page)
3. Check Render logs for download errors

**Fix:**
- Test download link in browser (should download file)
- Use direct Dropbox link (add `?dl=1` at end)

---

## 📁 Model File Hosting Options

### Option 1: Dropbox

1. Upload `best.pt` to Dropbox
2. Right-click → Share → Create link
3. Change `?dl=0` to `?dl=1` at end
4. Use this URL as `MODEL_URL`

### Option 2: Google Drive

1. Upload to Google Drive
2. Share → Anyone with link
3. Get file ID from URL
4. Use: `https://drive.google.com/uc?export=download&id=FILE_ID`

### Option 3: GitHub Releases

1. Create a GitHub release
2. Attach `best.pt` as asset
3. Use the asset download URL

---

## 💡 Tips for Free Tier

1. **Accept cold starts** - They're normal on free tier
2. **Use uptime monitor** - Keep app warm
3. **Monitor usage** - Check Render dashboard
4. **Optimize model** - Smaller model = faster loading
5. **Consider upgrade** - $7/month eliminates cold starts

---

## 🚀 Upgrade Options

If your app grows:

**Render Starter ($7/month):**
- ✅ No cold starts
- ✅ Always running
- ✅ Better resources

**Railway ($5/month):**
- ✅ No cold starts
- ✅ Better performance
- ✅ More flexibility

---

## 📊 Deployment Summary

| Aspect | Status |
|--------|--------|
| **Cost** | Free ✅ |
| **Setup** | 30 minutes ⏱️ |
| **Performance** | Good (with cold starts) ⚠️ |
| **Scalability** | Limited on free tier |
| **Reliability** | Good for low/medium traffic |

---

## 🎉 You're Live (for Free)!

Your YellowCert app is now:
- ✅ Deployed globally
- ✅ $0/month cost
- ✅ Auto-updating from Git
- ✅ Production URLs

Share your app:
```
🌐 https://yellowcert.vercel.app
```

**Note to users:** First load may take 30-60 seconds. Subsequent loads are fast!

---

## 📚 Next Steps

1. ✅ Test thoroughly
2. ✅ Set up UptimeRobot (avoid cold starts)
3. ✅ Monitor usage
4. ✅ Consider upgrade if needed
5. ✅ Share with users!

---

**Congratulations! Your YellowCert app is live for FREE! 🎉**
