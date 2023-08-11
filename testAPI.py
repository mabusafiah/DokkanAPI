from flask import Flask, jsonify, render_template, request
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace with your PostgreSQL connection details)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bingo@localhost/dokkan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://p5142_dokkan:Dokkan_2020@pgsql0.serv00.com:5432/p5142_dokkan'
db = SQLAlchemy(app)
#Dokkan_2020
#Define a model for a sample table:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
#Define a model for a settings:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
#Run Your Flask App:
#@app.route('/')
#def index():
#    return 'Hello, Flask!'



def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)


#This is the main function, that starts the server
if __name__ == '__main__':
    app.run()
    #app.run(port=8888)


msg = "hello there"
print(msg)