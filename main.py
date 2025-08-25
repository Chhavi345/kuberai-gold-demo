from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
database = []

@app.route("/gold-assistant", methods=["POST"])
def gold_assistant():
    user_input = request.json.get("query", "").lower()

    if "gold" in user_input:
        response = {
            "answer": "Gold is a safe investment during inflation. You can also buy digital gold using SimplifyMoney app.",
            "nudge": "Would you like to purchase 10 INR worth of digital gold?"
        }
    else:
        response = {"answer": "This is not related to gold investments."}
    
    return jsonify(response)

@app.route("/buy-gold", methods=["POST"])
def buy_gold():
    user = request.json.get("user", "Anonymous")
    amount = request.json.get("amount", 10)

    purchase = {
        "user": user,
        "amount": amount,
        "status": "success"
    }
    database.append(purchase)

    return jsonify({
        "message": f"{user} successfully purchased digital gold worth {amount} INR!",
        "database": database
    })

if __name__ == "__main__":
    app.run(debug=True)

