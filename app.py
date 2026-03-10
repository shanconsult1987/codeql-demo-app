from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "CodeQL Demo App"

@app.route("/user")
def get_user():

    user = request.args.get("id")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user

    cursor.execute(query)

    result = cursor.fetchall()

    return str(result)

app.run(host="0.0.0.0", port=5000)
