# app.py
# This is the brain of the web app.
# Python receives requests from the browser, talks to the database, and sends back pages.

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "chw2026"  # needed to remember who is logged in

# ── Step 1: Create the database and tables ──────────────────────────────────
def setup_database():
    conn = sqlite3.connect("chw.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            role     TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id           INTEGER PRIMARY KEY,
            chw_name     TEXT,
            patient_name TEXT,
            age          INTEGER,
            complaint    TEXT,
            referred     TEXT,
            date         TEXT
        )
    """)

    # Add demo users only if the table is empty
    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count == 0:
        conn.execute("INSERT INTO users VALUES (1, 'alice', 'alice123', 'chw')")
        conn.execute("INSERT INTO users VALUES (2, 'bob',   'bob123',   'chw')")
        conn.execute("INSERT INTO users VALUES (3, 'admin', 'admin123', 'supervisor')")

    conn.commit()
    conn.close()


# ── Step 2: Login page ───────────────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("chw.db")
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            # Save who is logged in
            session["username"] = user[1]
            session["role"]     = user[3]

            # Send CHW to their page, supervisor to theirs
            if user[3] == "chw":
                return redirect(url_for("chw_page"))
            else:
                return redirect(url_for("supervisor_page"))
        else:
            error = "Wrong username or password"

    return render_template("login.html", error=error)


# ── Step 3: CHW page — submit a visit report ─────────────────────────────────
@app.route("/chw", methods=["GET", "POST"])
def chw_page():
    if "username" not in session:
        return redirect(url_for("login"))

    message = ""
    if request.method == "POST":
        # Get what the CHW typed in the form
        patient = request.form["patient"]
        age     = request.form["age"]
        problem = request.form["problem"]
        refer   = request.form["refer"]

        # Save it to the database
        conn = sqlite3.connect("chw.db")
        conn.execute(
            "INSERT INTO reports (chw_name, patient_name, age, complaint, referred, date) VALUES (?,?,?,?,?,date('now'))",
            (session["username"], patient, age, problem, refer)
        )
        conn.commit()
        conn.close()

        message = "Report saved!"

    # Show all reports for this CHW
    conn = sqlite3.connect("chw.db")
    my_reports = conn.execute(
        "SELECT * FROM reports WHERE chw_name=?",
        (session["username"],)
    ).fetchall()
    conn.close()

    return render_template("chw.html", message=message, reports=my_reports, name=session["username"])


# ── Step 4: Supervisor page — see all reports ────────────────────────────────
@app.route("/supervisor")
def supervisor_page():
    if session.get("role") != "supervisor":
        return redirect(url_for("login"))

    conn = sqlite3.connect("chw.db")
    all_reports = conn.execute("SELECT * FROM reports").fetchall()
    conn.close()

    return render_template("supervisor.html", reports=all_reports)


# ── Step 5: Logout ───────────────────────────────────────────────────────────
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ── Run the app ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
