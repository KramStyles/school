from app import app, render_template

from functions import *
from config import *


@app.route('/add_admin')
def add_admin():
    return render_template("dashboard/add_admin.html")
