from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/register")
def register():
    return render_template('sign_up.html')

@auth.route('/register/personal')
def reg_personal():
    return render_template("r_personal.html")

@auth.route('/login')
def login():
    return render_template("login.html")