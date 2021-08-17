from app import app, render_template
from users import User
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from functions import *
from config import *

loginManager = LoginManager(app)


@loginManager.user_loader
def loadUser(username):
    return User(username)


@app.route('/add_admin')
@login_required
def add_admin():
    return render_template("dashboard/add_admin.html")


@app.route('/sign_in/<user>')
def sign_in(user):
    login_user(user)
    return render_template("dashboard/add_admin.html")


@app.route('/check')
def check():
    return current_user.get_id()
