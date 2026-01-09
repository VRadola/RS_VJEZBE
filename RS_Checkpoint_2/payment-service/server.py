from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, HTTPException
import requests
import os
import sqlite3
from db import init_db

TRANSACTION_SERVICE_URL = os.getenv("TRANSACTION_SERVICE_URL", "http://localhost:8002")
DB = "payments.db"

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

@app.post("/pay")
def pay(account_id: int, biller: str, amount: float, authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be > 0")

    # simulate bill payment by transferring to "biller account"
    # (in real system this would be external provider integration)
    r = requests.post(
        f"{TRANSACTION_SERVICE_URL}/transfer",
        params={"frm": account_id, "to": 999, "amount": amount, "note": f"Bill: {biller}"},
        headers={"Authorization": authorization}
    )
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Transaction service error")

    # log payment locally
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO payments(account_id, biller, amount) VALUES(?,?,?)",
        (account_id, biller, amount)
    )
    conn.commit()
    conn.close()

    return {"status": "paid", "biller": biller}

@app.get("/payments")
def list_payments(account_id: int, authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT id, account_id, biller, amount, timestamp
        FROM payments
        WHERE account_id = ?
        ORDER BY id DESC
        LIMIT 50
    """, (account_id,))

    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "account_id": r[1], "biller": r[2], "amount": r[3], "timestamp": r[4]}
        for r in rows
    ]