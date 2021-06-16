from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/register")
def register():
    return render_template('sign_up.html')

@auth.route('/register/personal')
def reg_personal():
    return render_template("r_personal.html")

@auth.route('/register/pacientes')
def reg_pacientes():
    return render_template("r_pacientes.html")

@auth.route('/register/procedimiento')
def reg_procedimientos():
    return render_template("r_procedimientos.html")

@auth.route('/login')
def login():
    return render_template("login.html")