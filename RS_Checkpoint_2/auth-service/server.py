from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from jose import jwt
from datetime import datetime, timedelta
import os

SECRET = os.getenv("JWT_SECRET", "secret")
ALGO = "HS256"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(username: str, password: str):
    if username != "user" or password != "pass":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGO)
    return {"access_token": token}
