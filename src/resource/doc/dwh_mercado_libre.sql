CREATE TABLE clientes (
id number  GENERATED BY DEFAULT ON NULL AS IDENTITY,
usuario varchar (50),
contrasenia varchar (100),
nombres varchar (50),
apellidos varchar (50),
fecha_nacimiento date,
telefono varchar(10),
estado varchar (1),
PRIMARY KEY (id)
);

CREATE TABLE categorias (
id number  GENERATED BY DEFAULT ON NULL AS IDENTITY,
nombre varchar (50),
estado varchar (1),
PRIMARY KEY (id)
);

CREATE TABLE productos (
id number  GENERATED BY DEFAULT ON NULL AS IDENTITY,
id_categorias int not null,
precio int not null,
cantidad int,
nombre varchar (50),
estado varchar (1),
PRIMARY KEY (id),
FOREIGN KEY (id_categorias) REFERENCES categorias (id)
);


CREATE TABLE compras (
id number  GENERATED BY DEFAULT ON NULL AS IDENTITY,
valor int ,
id_producto int,
id_cliente int,
fecha date,
forma_de_pago varchar(40),
estado varchar (1),
PRIMARY KEY (id),
FOREIGN KEY (id_producto) REFERENCES productos (id),
FOREIGN KEY (id_cliente) REFERENCES clientes (id)
);



