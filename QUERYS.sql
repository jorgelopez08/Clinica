
create table especialidades(
	id serial,
	descripcion varchar(50),
	primary key(id)
);

create table tipo_personal(
	id serial,
	descripcion varchar(50),
	primary key(id)
);


create table personal_medico(
	id serial,
	tipo_personal integer,
	curp varchar(19),
	nombre varchar(20),
	apellido_materno varchar(20),
	apellido_paterno varchar(20),
	fecha_nacimiento date,
	especialidad integer,
	primary key (id),
	constraint fk_especialidad foreign key (especialidad) references especialidades(id),
	constraint fk_tipo_personal foreign key (tipo_personal) references tipo_personal(id)
);	

create table pacientes(
	id serial,
	nombre varchar(20),
	apellido_materno varchar(20),
	apellido_paterno varchar(20),
	fecha_nacimiento date,
	alergias varchar(200),
	padecimiento varchar(200),
	primary key (id)
)

create table area(
	id serial,
	descripcion varchar(200),
	primary key(id)
)

create table administrativos(
	id serial,
	nombre varchar(20),
	apellido_materno varchar(20),
	apellido_paterno varchar(20),
	id_area integer,
	cobro decimal(10,2),
	primary key (id),
	constraint fk_id_area foreign key (id_area) references area(id)
);

create table cobro(
	id serial,
	id_administrativo integer,
	id_paciente integer,
	fecha date,
	cobro decimal(10,2),
	constraint fk_id_administrativo foreign key(id_administrativo) references administrativos(id),
	constraint fk_id_paciente foreign key (id_paciente) references pacientes(id)
);


create table mantenimiento(
	id serial,
	id_tipo_personal integer,
	area integer,
	primary key (id),
	constraint fk_id_tipo_persona foreign key (id_tipo_personal) references tipo_personal(id),
	constraint fk_area foreign key (area) references area(id)
);

create table historial_matenimineto(
	id serial,
	id_mantenimiento_realizado integer,
	fecha date, 
	descripcion varchar(200),
	primary key (id),
	constraint fk_id_mantenimineto_realizado foreign key (id_mantenimiento_realizado) references mantenimiento(id)
);

create table farmacia_receta(
	id serial,
	id_medico integer ,
	id_paciente integer,
	indicaciones varchar(200),
	primary key(id),
	constraint fk_id_medico foreign key (id_personal_medico) references personal_medico(id),
	constraint fk_id_paciente foreign key (id_paciente) references pacientes(id)
);

create table medicamentos (
	id serial,
	nombre varchar(20),
	presentacion integer,
	cantidad_disponible integer,
	primary key (id)
);

create table tipo_procedimiento(
	id serial,
	descripcion varchar(200),
	primary key(id)
);

create table procedimientos(
	id_paciente integer,
	id_personal_medico integer,
	id_tipo integer,
	nota varchar(200),
	fecha_entrada date,
	fecha_salida date,
	constraint fk_id_paciente foreign key (id_paciente) references pacientes(id),
	constraint fk_id_personal_medico foreign key (id_personal_medico) references personal_medico (id)
);


CREATE FUNCTION iva() RETURNS trigger
AS $add_iva$
BEGIN
    UPDATE cobro SET cobro = (NEW.cobro*1.16) WHERE id=NEW.id;
    RETURN NEW;
END;
$add_iva$ LANGUAGE plpgsql;

CREATE TRIGGER add_iva
    AFTER INSERT ON cobro
    FOR EACH ROW
    EXECUTE FUNCTION iva();


CREATE FUNCTION bono() RETURNS trigger
AS $add_bono$
BEGIN
    UPDATE administrativos SET sueldo = (NEW.cobro*1.10) WHERE id=NEW.id;
    RETURN NEW;
END;
$add_bono$ LANGUAGE plpgsql;

CREATE TRIGGER add_bono
    AFTER INSERT ON administrativos
    FOR EACH ROW
    EXECUTE FUNCTION descuento();