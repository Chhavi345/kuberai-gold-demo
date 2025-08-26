from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI(title="KuberAI Gold Demo")

# In-memory "database"
transactions = {}

# ---------------- API 1: Ask about Gold ----------------
class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_gold(req: AskRequest):
    question = req.question.lower()
    
    if "gold" in question or "invest" in question:
        return {
            "is_gold_related": True,
            "answer": "Gold is considered a safe-haven investment. You can start investing with as little as ₹10.",
            "nudge": "Would you like to purchase digital gold now?",
            "next_step": "/buy_gold"
        }
    else:
        return {
            "is_gold_related": False,
            "answer": "I can assist with finance queries. Try asking me about gold investments!"
        }

# ---------------- API 2: Buy Digital Gold ----------------
class BuyRequest(BaseModel):
    user_id: str
    amount: Optional[float] = 10.0 # default 10 if not provided

@app.post("/buy_gold")
def buy_gold(req: BuyRequest):
    txn_id = str(uuid4())
    transactions[txn_id] = {
        "user_id": req.user_id,
        "amount": req.amount,
        "status": "SUCCESS"
    }
    return {
        "status": "SUCCESS",
        "transaction_id": txn_id,
        "message": f"Digital Gold purchase successful for ₹{req.amount}"
    }

# ---------------- API 3: View Transactions ----------------
@app.get("/transactions")
def get_transactions():
    return transactions

# ---------------- Root Endpoint ----------------
@app.get("/")
def root():
    return {"message": "Welcome to KuberAI Gold Demo! Use /ask, /buy_gold, /transactions"}