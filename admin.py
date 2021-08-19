from app import app
from flask import render_template, redirect, request as re
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
    me = User(user)
    login_user(me)
    return render_template("dashboard/add_admin.html")


@app.route('/check/<info>')
def check(info):
    print("Info from check: ", info)
    return current_user.get_id()


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# METHODS

@app.route('/sign_in', methods=['POST'])
def sign():
    user = re.form.get('username')
    psword = re.form.get('pword')
    remember = re.form.get('remember')
    # remember = re.form['remember']
    rem = False
    if remember:
        rem = True
    # user = re.args.get('username')
    # psword = re.args.get('pword')
    # return check(f"Username: {user}, Password: {psword}, {rem}")
    if checkEmpty([user,psword]):
        msg = "Fill all fields"
    else:
        msg = "Login Valid"
    return msg