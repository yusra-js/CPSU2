from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
@app.route('/')

def index():
    return open('index.html').read()
@app.route('/submit_form', methods=['POST'])

def submit_form():
    name = request.form['name']
    email = request.form['email']
    
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return f"User {name} with email {email} has been added to the database!"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
