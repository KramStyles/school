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

@app.context_processor
def dash_all():
    info = {
        sitename: sitename
    }
    return dict(info=info)

@app.route('/add_admin')
@login_required
def add_admin():
    pg = {
        'title' : "add new user"
    }
    return render_template("dashboard/add_admin.html", pg=pg)


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
    if checkEmpty([user, psword]):
        msg = "Fill all fields"
    else:
        result = select('admin', f"WHERE username = '{user}'", 'password')
        if result:
            db_password = result[0][0]
            if verify(psword, db_password):
                me = User(user)
                login_user(me, remember=rem)
                msg = 'ok'
            else:
                msg = 'Invalid login details'
        else:
            msg = "User not found"
    return msg

# MY METHODS / ACTIONS

@app.route('/new_admin', methods=['POST'])
def new_admin():
    return "reached here"