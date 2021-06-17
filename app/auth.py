from flask import Blueprint, render_template, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Administrativos, Especialidades, Pacientes, Personal_medico, Procedimientos, Tipo_personal
from .config import Config

auth = Blueprint('auth', __name__)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(engine)
ses = Session()

@auth.route('/register')
def register():
    return render_template('sign_up.html')

@auth.route('/register/personal', methods=['GET','POST'])
def reg_personal():
    if request.method == 'POST':
        medico = Personal_medico(nombre = request.form.get('nombre'), apellido_materno = request.form.get('ap_mat'),
                                 apellido_paterno = request.form.get('ap_pat'), curp = request.form.get('curp'),
                                 tipo_personal = request.form.get('tipo'),
                                 fecha_nacimiento = request.form.get('cumpleanos'),
                                 especialidad = request.form.get('especialidad'))
        ses.add(medico)
        ses.commit()
        print(f'Values {medico.id} \n Form {request.form}')
        #Aquí debe de ir vista para success
    else:
        return render_template("r_personal.html")

@auth.route('/register/pacientes', methods=['GET','POST'])
def reg_pacientes():
    if request.method == 'POST':
        paciente = Pacientes(nombre = request.form.get('nombre'), apellido_materno = request.form.get('ap_mat'),
                             apellido_paterno = request.form.get('ap_pat'),
                             padecimiento = request.form.get('padecimiento'),
                             fecha_nacimiento = request.form.get('cumpleanos'), alergias = request.form.get('alergias'))
        ses.add(paciente)
        ses.commit()
        print(f'Values {paciente.id} \n Form {request.form}')
        #Aquí debe de ir vista para success
    else:
        return render_template("r_pacientes.html")

@auth.route('/register/procedimiento', methods=['GET','POST'])
def reg_procedimientos():
    if request.method == 'POST':
        procedimiento = Procedimientos(id_paciente=request.form.get('paciente'), id_personal_medico =
                                request.form.get('personal'), id_tipo = request.form.get('tipo'),
                                nota = request.form.get('nota'), fecha_entrada = request.form.get('entrada'),
                                fecha_salida = request.form.get('salida'))
        ses.add(procedimiento)
        ses.commit()
        print(f'Values {procedimiento.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html")

@auth.route('/register/procedimiento', methods=['GET','POST'])
def reg_procedimientos():
    if request.method == 'POST':
        procedimiento = Procedimientos(id_paciente=request.form.get('paciente'), id_personal_medico =
                                request.form.get('personal'), id_tipo = request.form.get('tipo'),
                                nota = request.form.get('nota'), fecha_entrada = request.form.get('entrada'),
                                fecha_salida = request.form.get('salida'))
        ses.add(procedimiento)
        ses.commit()
        print(f'Values {procedimiento.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html")

@auth.route('/login', methods=['GET','POST'])
def login():
        return render_template("login.html")