from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, HTTPException
from jose import jwt
import requests
import os
import sqlite3
from db import init_db

SECRET = os.getenv("JWT_SECRET", "secret")
ALGO = "HS256"
ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:8001")
DB = "transactions.db"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

def require_auth(authorization: str | None):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.replace("Bearer ", "", 1)
    try:
        jwt.decode(token, SECRET, algorithms=[ALGO])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/transfer")
def transfer(frm: int, to: int, amount: float, note: str = "", authorization: str | None = Header(default=None)):
    require_auth(authorization)

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be > 0")

    if frm == to:
        raise HTTPException(status_code=400, detail="Cannot transfer to the same account")

    r1 = requests.post(
        f"{ACCOUNT_SERVICE_URL}/accounts/{frm}/update",
        params={"amount": -amount}
    )

    if r1.status_code != 200:
        raise HTTPException(status_code=400, detail="Debit failed")

    if to != 999:
        r2 = requests.post(
            f"{ACCOUNT_SERVICE_URL}/accounts/{to}/update",
            params={"amount": amount}
        )

        if r2.status_code != 200:
            # rollback
            requests.post(
                f"{ACCOUNT_SERVICE_URL}/accounts/{frm}/update",
                params={"amount": amount}
            )
            raise HTTPException(status_code=400, detail="Credit failed")


    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions(from_account, to_account, amount, note) VALUES(?,?,?,?)",
        (frm, to, amount, note)
    )
    conn.commit()
    conn.close()

    return {"status": "completed"}

@app.get("/transactions")
def list_transactions(account_id: int, authorization: str | None = Header(default=None)):
    require_auth(authorization)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
    SELECT id, from_account, to_account, amount, note, timestamp
    FROM transactions
    WHERE from_account = ? OR to_account = ?
    ORDER BY id DESC
    LIMIT 50
""", (account_id, account_id))

    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "from": r[1], "to": r[2], "amount": r[3], "note": r[4], "timestamp": r[5]}
    for r in rows
    ]