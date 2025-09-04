from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import os
from model import analyze_retina

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    # Save uploaded image
    image_path = f"uploads/{image.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Run analysis
    result = analyze_retina(image_path)

    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
