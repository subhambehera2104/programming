from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

# import pymysql
# pymysql.install_as_MySQLdb()

# app = Flask(__name__)

# username = 'flask_app'
# password = '12345678'
# host = 'localhost'
# port = 3306
# DB_NAME = 'todo_db'


#mysql_url = f"mysql+pymysql://{username}:{password}@{host}:{port}"
# app.config['SQLALCHEMY_DATABASE_URI']= mysql_url


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)


class Todo(db.Model):
    task_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    done=db.Column(db.Boolean)

@app.route('/')
def home():
    todo_list=Todo.query.all()
    return render_template('base.html',todo_list=todo_list)

@app.route('/add',methods=['POST'])
def add():
    name = request.form.get("name")
    new_task=Todo(name=name,done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo= Todo.query.get(todo_id)
    todo.done=not todo.done
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo= Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))



if __name__=='__main__':
     with app.app_context():
        db.create_all()
     app.run(host='0.0.0.0', port=5002, debug=True)