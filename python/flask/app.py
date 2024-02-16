from flask import Flask, request, session, redirect, url_for, render_template, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "subhAM123$%"

db = mysql.connector.connect(
    host="localhost",
    user="flask_app",
    password="12345678",
    database="flask_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register_page', methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route('/register', methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    phone = request.form["phone"]
    gender = request.form["gender"]

    hashed_password = generate_password_hash(password)

    insert_query = "INSERT INTO users (name, email, password, phone, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, email, hashed_password, phone, gender))
    db.commit()
  
    flash("You were successfully registered")
    return redirect(url_for("home"))

@app.route('/login_page', methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    email= request.form["email"]
    password = request.form["password"]

    sql = "SELECT password FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    row = cursor.fetchone()

    if row and check_password_hash(row[0], password): 
        # row[0] is password column wheere hashed password is stored
        session["email"] = email 
        flash("Login success")
        return redirect(url_for("home"))
    else:
        flash("Invalid email or password")
        return render_template("login.html")

app.run(host='0.0.0.0', port=5001, debug=True)
