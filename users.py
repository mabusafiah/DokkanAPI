#import os
import psycopg2
import json
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dandan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bingo@localhost/dokkan' 

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# API endpoint for login
@app.route('/api/login', methods=['POST'])
def api_login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email, password=password).first()

    if user:
        login_user(user)
        #return jsonify(user)
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'message': 'Invalid email or password'}), 401


    
# Protected API endpoint
@app.route('/api/protected', methods=['GET'])
@login_required
def api_protected():
    return jsonify({'message': 'You have access to this protected resource'})



'''''
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='dokkan',
                            user='postgres',
                            password='Bingo')
    return conn
''''''

@app.route('/users', methods=['GET'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('users/index.html', users=users)


@app.route('/usersx', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)


@app.route('/users/create/', methods=('GET', 'POST'))
def create():
    return render_template('users/create.html')


@app.route('/users/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
     
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, email)'
                    'VALUES (%s, %s)',
                    (username, email))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('users/create.html')




@app.route('/users/login', methods=['POST'])
def login():
    #email = request.json.get('email')
    #password = request.json.get('password')

    password = request.form['password']
    email = request.form['email']

    user = user.query.filter_by(email=email, password=password).first()

    if user:
        # User exists, perform successful login action
        return jsonify({'message': 'Login successful'}), 200
    else:
        # User not found or incorrect credentials
        return jsonify({'message': 'Invalid credentials'}), 401

   # return jsonify(users)

'''
   
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
    app.run(port=5000)
   #if __name__ == "__main__":
   # from waitress import serve
   # serve(app, host="0.0.0.0", port=8080)