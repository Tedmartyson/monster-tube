from app import app, db
from flask import render_template
from app.models import User

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
