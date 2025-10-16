# practice_server.py
"""
Tiny Flask server to practice the brute-force demo.
This server has one user:
    username: admin
    password: secret123
Run this locally: python practice_server.py
Then run the bruteforce demo targeting http://127.0.0.1:5000/login
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Very simple 'user database' (do NOT use in production)
USERS = {"admin": "secret123"}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")
    if USERS.get(username) == password:
        return jsonify({"result": "success", "message": "Welcome!"}), 200
    else:
        return jsonify({"result": "failure", "message": "Invalid credentials"}), 401

@app.route("/")
def index():
    return "Practice server: POST JSON to /login with username & password"

if __name__ == "__main__":
    # Only for local testing (do not expose publicly)
    app.run(host="127.0.0.1", port=5000, debug=False)
