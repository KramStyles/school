from app import app
from flask import render_template, redirect, request
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


@app.route('/sign_in', methods=['POST '])
def sign():
    # user = request.form.get('username')
    # psword = request.form.get('pword')
    # user = request.args.get('username')
    # psword = request.args.get('pword')
    user = request.form['username']
    psword = request.form['pword']
    return f"Username: {user}, Password: {psword}"


@app.route('/sign_in/<user>')
def sign_in(user):
    me = User(user)
    login_user(me)
    return render_template("dashboard/add_admin.html")


@app.route('/check')
def check():
    return current_user.get_id()


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')
