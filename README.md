# retinascan-prot
# RetinaScan Prot 🧠📸  
AI-powered retinal scan analysis with FastAPI, Grad-CAM overlays, and Supabase logging.

## 🚀 Live Demo  
**Backend URL:** `https://retinascan-prot.onrender.com`  
**Health Check:** [`/health`](https://retinascan-prot.onrender.com/health)

---

## 🧩 Features

- 🔍 `/analyze` endpoint for retinal image classification
- 🧠 Grad-CAM overlay generation for visual interpretability
- 📊 Confidence scoring + severity mapping
- 📝 `/feedback` endpoint for clinician annotations
- 🗂️ Supabase logging for scan history and analytics
- 🌐 CORS-enabled for frontend integration

---

## 📦 Tech Stack

- **FastAPI** for backend API
- **Torch** for model inference
- **Pillow / OpenCV** for image handling
- **Supabase** for logging and feedback
- **Render** for deployment

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/momaxx/retinascan-backend.git
cd retinascan-backend

