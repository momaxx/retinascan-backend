import os
import uuid
import requests
from datetime import datetime

def log_scan_to_supabase(image_name, confidence, severity, gradcam_url):
    # Load from environment variables
    supabase_url = os.getenv("https://dbmjyboohplgtcoqlmen.supabase.co")
    supabase_key = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRibWp5Ym9vaHBsZ3Rjb3FsbWVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY5NzI4MzUsImV4cCI6MjA3MjU0ODgzNX0.JhhxveJAEZ6oxiGl5gozMlgAkJFQ_-dWDyxwTfh6kQ0")

    if not supabase_url or not supabase_key:
        print("Supabase credentials missing")
        return

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRibWp5Ym9vaHBsZ3Rjb3FsbWVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY5NzI4MzUsImV4cCI6MjA3MjU0ODgzNX0.JhhxveJAEZ6oxiGl5gozMlgAkJFQ_-dWDyxwTfh6kQ0}",
        "Content-Type": "application/json"
    }

    payload = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "image_name": image_name,
        "confidence": confidence,
        "severity": severity,
        "gradcam_url": gradcam_url
    }

    try:
        response = requests.post(
            f"{supabase_url}/rest/v1/scan_logs",
            headers=headers,
            json=payload
        )
        print("Supabase log response:", response.status_code, response.text)
    except Exception as e:
        print("Error logging to Supabase:", str(e))
