from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt
import sqlite3, os
from db import init_db

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
DB = "accounts.db"

@app.on_event("startup")
def startup():
    init_db()

def verify(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

def auth_dep(authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.replace("Bearer ", "", 1)
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/accounts/{id}")
def get_balance(id: int, user=Depends(auth_dep)):
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id=?", (id,))
    row = cur.fetchone()
    db.close()

    if not row:
        raise HTTPException(status_code=404, detail="Account not found")

    return {"balance": row[0]}

@app.post("/accounts/{id}/update")
def update_balance(id: int, amount: float):
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (amount, id))
    if cur.rowcount == 0:
        db.close()
        raise HTTPException(status_code=404, detail="Account not found")
    db.commit()
    db.close()
    return {"status": "updated"}

@app.get("/accounts")
def list_accounts(user=Depends(auth_dep)):
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("SELECT id, owner, balance FROM accounts")
    rows = cur.fetchall()
    db.close()

    return [
        {"id": r[0], "name": r[1], "balance": r[2]}
        for r in rows
    ]

