from flask import Flask, render_template, request, redirect, url_for
from database import db_session
from models import User, Exercise, Progress

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handle registration logic
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login logic
    pass

@app.route('/progress')
def progress():
    # Display user's progress
    pass

if __name__ == '__main__':
    app.run(debug=True)
