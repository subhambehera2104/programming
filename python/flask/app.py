from flask import Flask, request, session, render_template, url_for, flash, redirect
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "subhAM123$%"

UPLOAD_FOLDER = 'static/images/uploads/profile'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


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

@app.route("/user/register_page", methods=['GET'])
def register_page():
    return render_template("register.html")


@app.route("/user/register", methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    gender = request.form['gender']


    hashed_password = generate_password_hash(password)
    insert_query = "INSERT INTO users (name, email, password, phone, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, email, hashed_password, phone, gender))
    db.commit()
    
    flash("You were successfully registered")
    return render_template("home.html", data={"name": name})


@app.route('/user/login_page', methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route('/user/login', methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    sql= "SELECT id, name, password FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    row= cursor.fetchone()
    if row and check_password_hash(row[2], password):
        #row[0] is password column where haashed password is stored
        session["email"] = email
        flash("login success")
        return render_template("home.html", data={"user_id": row[0], "name": row[1]})
    else:
        flash("Invalid email or password")
        return render_template("index.html", error="Login failed")


@app.route("/user/<user_id>", methods=['GET'])
def user_profile(user_id):
    user_id = request.view_args['user_id']
    sql = "SELECT name, email, phone, profile_image from users WHERE id=%s"
    cursor.execute(sql, (user_id,))
    row = cursor.fetchone()
    if row:
        return render_template("profile.html", data= {"user_id": user_id, "name": row[0], "email": row[1], "phone": row[2], "user_profile_image": row[3]})
    else:
        return "User not found"

def _search_helper(name):
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

@app.route('/user/search', methods=['GET'])
def search_by_query_param():
    args = request.args
    name = args.get('name') # ? query param
    return _search_helper(name)

@app.route('/user/search', methods=['POST'])
def search():
    name = request.form["name"]
    return _search_helper(name)
 
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

@app.route('/user/change_password/<user_id>', methods=["POST"])
def change_password(user_id):
    old_password = request.form['old password']
    new_password = request.form['new password']
    confirm_password = request.form['confirm password']
    if new_password == confirm_password:
        sql = "SELECT id, name, password FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        row= cursor.fetchone()
        if row and check_password_hash(row[2], password):
            hashed_password = generate_password_hash(new_password)
            sql = "UPDATE users SET password= %s WHERE id = %s"
            cursor.execute(sql, (hashed_password, user_id,))
            db.commit()
            return "success"
        else:
            return render_template("base/error.html",  data = { "user_id": user_id, "message": "Old Password is wrong"})
    else:
        return render_template("base/error.html", data = { "user_id": user_id, "message": "New password doesn't match with confirm password"})

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower() 

def allowed_file(filename):
    return '.' in filename and get_file_extension(filename) in ALLOWED_EXTENSIONS

@app.route('/user/upload_img/<user_id>', methods=['POST'])
def upload_image(user_id):  
    try:
        if 'file' not in request.files:
            flash('File not found')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            save_filename = f"{user_id}_{(file.filename)}"
            file.save(os.path.join(UPLOAD_FOLDER, save_filename))
            # todo write sql update query to update profle_image column
            sql = "UPDATE users SET profile_image=%s WHERE id =%s"
            cursor.execute(sql, (save_filename, user_id,))
            db.commit()
            return redirect(url_for('user_profile', user_id =user_id))
    except Exception as err:
        return render_template("base/error.html",  data = { "user_id": user_id, "message": str(err)})

@app.route('/user/admin_panel', methods=['POST'])
def admin_pannel():
    return render_template("admin.html")

@app.route('/user/signout/<user_id>', methods=["POST"])
def signout(user_id):
    return render_template("index.html")

@app.route('/user/generate_otp', methods=['POST'])
def generate_otp():
    email = request.form['email']
    otp=1234
    sql = "UPDATE users SET otp=%s WHERE email=%s"
    cursor.execute(sql, (otp, email))
    db.commit()
    return render_template("index.html")

@app.route('/user/veryfi_otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    otp = request.form['otp']
    sql = "SELECT otp FORM users WHERE email=%s"
    cursor.execute(sql, (email,))
    row = cursor.fetchone()
    if row[0] == otp:
        return render_template("home.html")
    else:
        return "Your login faield! Please try agin"
    

app.run(host='0.0.0.0', port=5001, debug=True)