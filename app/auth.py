from flask.helpers import url_for
from app import views
from flask import Blueprint, render_template, request, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Administrativos, Especialidades, Pacientes, Personal_medico, Procedimientos, Tipo_personal, Area, \
    Cobro, Medicamentos, Tipo_procedimiento
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
        return redirect(url_for('views.doctores'))
        #Aquí debe de ir vista para success
    else:
        return render_template("r_personal.html")

@auth.route('/register/personal/<int:id>', methods=['POST'])
def update_personal(id):
    ses.query(Personal_medico).filter_by(id = id).update(dict(nombre = request.form.get('nombre'), apellido_materno =
                             request.form.get('ap_mat'),
                             apellido_paterno = request.form.get('ap_pat'), curp = request.form.get('curp'),
                             tipo_personal = request.form.get('tipo'),
                             fecha_nacimiento = request.form.get('cumpleanos'),
                             especialidad = request.form.get('especialidad')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    #Aquí debe de ir vista para success

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
        return redirect(url_for('views.pacientes'))
        #Aquí debe de ir vista para success
    else:
        return render_template("r_pacientes.html")

@auth.route('/register/pacientes/<int:id>', methods=['PUT'])
def update_pacientes(id):
    ses.query(Pacientes).filter_by(id = id).update(dict(nombre = request.form.get('nombre'), apellido_materno =
                         request.form.get('ap_mat'),
                         apellido_paterno = request.form.get('ap_pat'),
                         padecimiento = request.form.get('padecimiento'),
                         fecha_nacimiento = request.form.get('cumpleanos'), alergias = request.form.get('alergias')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    #Aquí debe de ir vista para success

@auth.route('/register/procedimiento', methods=['GET','POST'])
def reg_procedimientos():
    if request.method == 'POST':
        procedimiento = Procedimientos(id_paciente=request.form.get('id_paciente'), id_personal_medico =
                                request.form.get('id_personal'), id_tipo = request.form.get('tipo'),
                                nota = request.form.get('nota'), fecha_entrada = request.form.get('entrada'),
                                fecha_salida = request.form.get('salida'))
        ses.add(procedimiento)
        ses.commit()
        print(request.form.get('tipo'))
        print(f'Values {procedimiento.id} \n Form {request.form}')
        return redirect(url_for('views.procedimientos'))
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html")

@auth.route('/register/procedimiento/<int:id>', methods=['PUT'])
def update_procedimientos(id):
    ses.query(Procedimientos).filter_by(id = id).update(dict( id_paciente=request.form.get('paciente'),
                                   id_personal_medico = request.form.get('personal'), id_tipo = request.form.get('tipo')
                                   , nota = request.form.get('nota'), fecha_entrada = request.form.get('entrada'),
                                   fecha_salida = request.form.get('salida')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    # Aquí debe de ir vista para success

@auth.route('/register/cat-especialidad', methods=['GET','POST'])
def reg_especialidad():
    if request.method == 'POST':
        especialidad = Especialidades(descripcion = request.form.get('descripcion'))
        ses.add(especialidad)
        ses.commit()
        print(f'Values {especialidad.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de especialidad

@auth.route('/register/cat-especialidad/<int:id>', methods=['PUT'])
def update_especialidad(id):
    ses.query(Especialidades).filter_by(id = id).update(dict( descripcion = request.form.get('descripcion')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    # Aquí debe de ir vista para success
    
@auth.route('/register/cat-tipo-personal', methods=['GET','POST'])
def reg_tipo_personal():
    if request.method == 'POST':
        tipoPersonal = Tipo_personal(descripcion = request.form.get('descripcion'))
        ses.add(tipoPersonal)
        ses.commit()
        print(f'Values {tipoPersonal.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de tipo de personal

@auth.route('/register/cat-tipo-personal/<int:id>', methods=['PUT'])
def update_tipo_personal(id):
    ses.query(Tipo_personal).filter_by(id = id).update(dict( descripcion = request.form.get('descripcion')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    # Aquí debe de ir vista para success

@auth.route('/register/cat-area', methods=['GET','POST'])
def reg_area():
    if request.method == 'POST':
        area = Area(descripcion = request.form.get('descripcion'))
        ses.add(area)
        ses.commit()
        print(f'Values {area.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de área

@auth.route('/register/cat-area/<int:id>', methods=['PUT'])
def update_area(id):
    ses.query(Area).filter_by(id = id).update(dict( descripcion = request.form.get('descripcion')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    # Aquí debe de ir vista para success

@auth.route('/register/administrativo', methods=['GET','POST'])
def reg_administrativo():
    if request.method == 'POST':
        admin = Administrativos(nombre = request.form.get('nombre'), apellido_materno = request.form.get('ap_mat'),
                                apellido_paterno = request.form.get('ap_pat'), id_area = request.form.get('area'))
        ses.add(admin)
        ses.commit()
        print(f'Values {admin.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de tipo de personal

@auth.route('/register/administrativo/<int:id>', methods=['PUT'])
def update_administrativo(id):
    ses.query(Administrativos).filter_by(id = id).update(dict( nombre = request.form.get('nombre'), apellido_materno =
                            request.form.get('ap_mat'),
                            apellido_paterno = request.form.get('ap_pat'), id_area = request.form.get('area')))
    ses.commit()
    print(f'Values {id} \n Form {request.form}')
    # Aquí debe de ir vista para success

@auth.route('/register/cobro', methods=['GET','POST'])
def reg_cobro():
    if request.method == 'POST':
        cobro = Cobro(id_administrativo = request.form.get('admin_id'), id_paciente = request.form.get('paciente_id'),
                      fecha = request.form.get('fecha'), cobro = request.form.get('total'))
        ses.add(cobro)
        ses.commit()
        print(f'Values {cobro.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de tipo de personal

@auth.route('/register/medicamento', methods=['GET','POST'])
def reg_medicamento():
    if request.method == 'POST':
        medicamento = Medicamentos(nombre = request.form.get('nombre'), presentacion = request.form.get('presentacion'),
                                   cantidad_disponible = request.form.get('stock'))
        ses.add(medicamento)
        ses.commit()
        print(f'Values {medicamento.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de tipo de personal

@auth.route('/register/cat-tipo-procedimiento', methods=['GET','POST'])
def reg_tipo_procedimientos():
    if request.method == 'POST':
        tipoProcedimiento = Tipo_procedimiento(descripcion = request.form.get('descripcion'))
        ses.add(tipoProcedimiento)
        ses.commit()
        print(f'Values {tipoProcedimiento.id} \n Form {request.form}')
        # Aquí debe de ir vista para success
    else:
        return render_template("r_procedimientos.html") #ToDo:Cambiar a pantalla de registro de área


@auth.route('/login', methods=['GET','POST'])
def login():
        return render_template("login.html")