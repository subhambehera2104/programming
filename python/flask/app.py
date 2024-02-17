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

@app.route("/user/register_page", methods=['GET'])
def register_page():
    return render_template("register.html")


@app.route("/user/register", methods=['POST'])
def register():
    
    name = request.form['name']
    emai = request.foprm['email']
    password = request.form['password']
    phone = request.form['phone']
    gender = request.form['m']
    gender = request.form['f']

    hashed_password = generate_password_hash(password)
    insert_query = "INSERT INTO users (name, email, password, phone, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, email, hashed_password, phone, gender))
    db.commit()
    
    flash("You were successfully registered")
    return redirect(url_for('home'))

@app.route('/user/login_page', methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route('/user/login', methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    sql= "SELECT password FROM user WHERE email = %s"
    cursor.execute(sql, (email,))
    row= cursor.fetchone()
    if row and check_password_hash(row[0], password):
        #row[0] is password column where haashed password is stored
        session["email"] = emai
        flash("login susccess")
        return render_template(url_for("home"))
    else:
        flash("Invalid email or password")
        return render_template("login.html")


@app.route("/user/<user_id>", methods=['GET'])
def user_profile(user_id):
    user_id = request.view_args['user_id']
    sql = "SELECT name, email, phone FROM users WHERE id =%s"
    cursor.execute(sql, (user_id,))
    row = cursor.fetchone()
    if row:
        return render_template("profile.html", data= {"user_id": user_id, "name": row[0], "email": row[1], "phone": row[2]})
    else:
        return "User not found"


@app.route('/user/search', methods=['GET'])
def search():
    args = request.args
    name = args.get('name')
    sql = f"SELECT id, name, email, phone FROM users WHERE name like '{name}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    results = []
    for row in rows:
        results.append(
            {
              "user_id": row[0],
              "name": row[1], 
              "email": row[2],
              "phone": row[3]
            }
        )
    if rows:
        return render_template("user_search.html", results = results)
    else:
        return "User not found"

 
@app.route('/user/delete/<user_id>', methods=["POST"])
def user_delete(user_id):
    user_id = request.view_args['user_id']
    sql = "DELETE FROM users WHERE id =%s"
    cursor.execute(sql, (user_id,))
    return "User deleted successfully"  

@app.route("/user/update_page/<user_id>", methods=['GET'])
def user_update_page(user_id):
    user_id = request.view_args['user_id']
    sql = "SELECT name, email, phone FROM users WHERE id =%s"
    cursor.execute(sql, (user_id,))
    row = cursor.fetchone()
    if row:
        return render_template("update.html", data= {"user_id": user_id, "name": row[0], "email": row[1], "phone": row[2]})
    else:
        return "User not found" 

@app.route('/user/update/<user_id>', methods=["POST"])
def user_update(user_id):
    user_id = request.view_args['user_id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    sql = "UPDATE users SET name = %s, email = %s , phone=%s WHERE id = %s"
    cursor.execute(sql, (name, email, phone, user_id))
    db.commit()
    
    return "User updated successfully" 

  


app.run(host='0.0.0.0', port=5001, debug=True)