from flask import Flask, request, jsonify, render_template
from db import get_connection

app = Flask(__name__)

# login page
@app.route("/")
def login_page():
    return render_template("login.html")

# API login route
@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
