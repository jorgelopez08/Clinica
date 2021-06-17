from flask import Blueprint, render_template
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from .models import Administrativos, Especialidades, Pacientes, Personal_medico, Procedimientos, Tipo_personal
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
ses = Session()
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/pacientes')
def pacientes():
    context = {
        'title':"Pacientes",
        'datos':Pacientes.query.all()
    }
    return render_template("show.html",**context)

@views.route('/doctores')
def doctores():
    context = {
        'title':"Personal médico",
        'tipo':Tipo_personal.query.all(),
        'extra':Especialidades.query.all(),
        'datos':Personal_medico.query.all()
    }
    return render_template("show.html", **context)

@views.route('/admin')
def admin():
    context = {
        'title':"Administrativos",
        'tipo':Tipo_personal.query.all(),
        'extra':Especialidades.query.all(),
        'datos':Administrativos.query.all()
    }
    return render_template("show.html", **context)

@views.route('/procedimientos')
def procedimientos():
    context = {
        'title':"Procedimientos",
        'datos':Procedimientos.query.all()
    }
    return render_template("show.html", **context)