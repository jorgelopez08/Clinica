from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Pacientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    #curp = db.Column(db.String(18), unique=True)
    fecha_nacimiento = db.Column(db.Date)
    apellido_paterno = db.Column(db.String(20))
    apellido_materno = db.Column(db.String(20))
    alergias = db.Column(db.String(200))
    padecimiento = db.Column(db.String(200))

class Personal_medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_personal = db.Column(db.Integer, db.ForeignKey("Tipo_personal.id"), nullable=False)
    curp = db.Column(db.String(18), unique=True)
    nombre = db.Column(db.String(20))
    apellido_paterno = db.Column(db.String(20))
    apellido_materno = db.Column(db.String(20))
    fecha_nacimiento = db.Column(db.Date)
    especialidad = db.Column(db.Integer, db.ForeignKey("Especialidades.id"))

class Especialidades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

class Tipo_personal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))

class Administrativos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido_paterno = db.Column(db.String(20))
    apellido_materno = db.Column(db.String(20))
    id_area = db.Column(db.Integer, db.ForeignKey("Area.id"))

class Cobro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_administrativo = db.Column(db.Integer, db.ForeignKey("Administrativos.id"))
    id_paciente = db.Column(db.Integer, db.ForeignKey("Pacientes.id"))
    fecha = db.Column(db.Date)
    cobro = db.Column(db.Float)

''' class Mantenimiento(db.Model):
    pass

class Historial_mantenimiento(db.Model):
    pass '''

class Farmacia_receta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_medico = db.Column(db.Integer, db.ForeignKey("Personal_medico.id"))
    id_paciente = db.Column(db.Integer, db.ForeignKey("Pacientes.id"))
    indicaciones = db.Column(db.String(200))

class Medicamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    presentación = db.Column(db.Integer)
    cantidad_disponible = db.Column(db.Integer)

class Tipo_procedimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))

class Procedimientos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey("Pacientes.id"))
    id_personal_medico = db.Column(db.Integer, db.ForeignKey("Personal_medico.id"))
    nota = db.Column(db.String(200))
    fecha_entrada = db.Column(db.Date)
    fecha_salida = db.Column(db.Date)
    