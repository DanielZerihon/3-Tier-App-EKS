from flask import Flask, request, render_template
from db import get_connection

app = Flask(__name__)

# login screen
@app.route("/")
def login_page():
    return render_template("login.html")

# login
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

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
        return render_template("success.html")

    return render_template("login.html", error="user name or pass incorrect")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
