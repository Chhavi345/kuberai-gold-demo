from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI(title="KuberAI Gold Demo")

# Mock DB
transactions = {}

# -------- API 1: Ask about Gold ------------
class AskRequest(BaseModel):
    user_id: str
    question: str

@app.post("/ask")
def ask_gold(req: AskRequest):
    question = req.question.lower()

    # Detect intent for gold investment
    if "gold" in question or "digital gold" in question or "invest" in question:
        response = {
            "answer": "Gold is often considered a safe-haven investment. You can start with as little as ₹10.",
            "nudge": "Would you like to purchase digital gold now?",
            "next_step": "/buy_gold"
        }
    else:
        response = {
            "answer": "I can assist with finance queries. Try asking me about gold investments!",
            "nudge": None,
            "next_step": None
        }
    return response


# -------- API 2: Buy Digital Gold ------------
class BuyRequest(BaseModel):
    user_id: str
    amount: Optional[float] = 10.0 # default ₹10

@app.post("/buy_gold")
def buy_gold(req: BuyRequest):
    txn_id = str(uuid.uuid4())
    transactions[txn_id] = {
        "user_id": req.user_id,
        "amount": req.amount,
        "status": "SUCCESS"
    }

    return {
        "message": f"Digital Gold purchase successful for ₹{req.amount}",
        "transaction_id": txn_id,
        "user_id": req.user_id,
        "status": "SUCCESS"
    }


# -------- API 3: View Transactions --------
@app.get("/transactions")
def get_transactions():
    return transactions