from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Add this root endpoint
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RetinaScan App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            h1 { color: #2563eb; }
            .links { margin-top: 20px; }
            .links a { display: inline-block; margin-right: 15px; color: #2563eb; text-decoration: none; }
            .links a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 RetinaScan Application</h1>
            <p>Your FastAPI application is successfully deployed on Render!</p>
            
            <div class="links">
                <h3>Quick Links:</h3>
                <a href="/docs">API Documentation</a>
                <a href="/redoc">Alternative Docs</a>
                <a href="/dashboard">Dashboard</a>
            </div>
            
            <div style="margin-top: 30px; padding: 15px; background: #f0f9ff; border-radius: 5px;">
                <strong>Next Steps:</strong>
                <p>Add your specific endpoints and dashboard functionality in the app/main.py file</p>
            </div>
        </div>
    </body>
    </html>
    """

# Add your other endpoints below this
@app.get("/dashboard")
async def dashboard():
    return {"message": "Dashboard endpoint - implement your dashboard here"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "retinascan-backend"}
