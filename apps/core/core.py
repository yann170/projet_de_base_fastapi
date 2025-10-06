
import os

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.50.250", 
    "https://hotspot.mikrotik.com", 
    "https://votre-frontend-en-ligne.netlify.app",
    "https://votre-url-fastapi.onrender.com",
    os.getenv("FRONTEND_URL", "http://localhost:3000") 
]