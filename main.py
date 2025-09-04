from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import shutil
from model import analyze_retina

app = FastAPI()

# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    try:
        image_path = f"uploads/{image.filename}"
        os.makedirs("uploads", exist_ok=True)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        result = analyze_retina(image_path)
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# 🔥 This is the critical part for Railway
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
source /app/.venv/bin/activate
python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    try:
        image_path = f"uploads/{image.filename}"
        os.makedirs("uploads", exist_ok=True)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        result = analyze_retina(image_path)
        return JSONResponse(content=result)

    except Exception as e:
        print("Error during analysis:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}
https://retinascan-pro.onrender.com/health


