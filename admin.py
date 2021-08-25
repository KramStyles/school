from app import app
from flask import render_template, redirect, request as req
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
        'title': "add new user"
    }
    return render_template("dashboard/add_admin.html", admin_info=pg)

@app.route('/admin_list')
@login_required
def admin_list():
    admins = select('admin')
    pg = {
        'title': "admins",
        'admins': admins
    }
    return render_template("dashboard/admin_list.html", admin_info=pg)


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


# MY METHODS / ACTIONS

@app.route('/sign_in', methods=['POST'])
def sign():
    user = req.form.get('username')
    psword = req.form.get('pword')
    remember = req.form.get('remember')
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


@app.route('/new_admin', methods=['POST'])
def new_admin():
    username = req.form['username'].lower()
    fname = req.form['fname'].title()
    mobile = req.form['mobile']
    email = req.form['email']
    psword = req.form['password']
    confirm = req.form['confirm']
    address = req.form['address']
    if checkEmpty([username, fname, email, psword, confirm]):
        msg = "All fields are important."
    elif select('admin', f"where username = '{username}'"):
        msg = "Username already exists"
    elif select('admin', f"where email = '{email}'"):
        msg = "Email address already in use"
    elif len(psword) < 5:
        msg = "Your password is too short"
    elif confirm != psword:
        msg = "Your passwords do not match"
    else:
        psword = password(psword)
        regdate = datetime.now()
        msg = db_insert('admin', "username, name, mobile, email, address, password, regdate",
                  f"'{username}','{fname}','{mobile}','{email}','{address}','{psword}','{regdate}'")
    return msg


