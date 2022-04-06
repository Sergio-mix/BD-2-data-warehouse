CREATE TABLE clientes (
id int AUTO_INCREMENT NOT NULL,
usuario varchar (50),
contrasenia varchar (100),
nombres varchar (50),
apellidos varchar (50),
edad int,
telefono int,
estado varchar (1),
PRIMARY KEY (id));

CREATE TABLE pagos (
id int AUTO_INCREMENT NOT NULL,
forma_de_pago int ,
estado varchar (1),
PRIMARY KEY (id));

CREATE TABLE categorias (
id int AUTO_INCREMENT NOT NULL,
nombre varchar (50),
estado varchar (1),
PRIMARY KEY (id));

CREATE TABLE productos (
id int AUTO_INCREMENT NOT NULL,
id_categorias int not null,
precio int not null,
cantidad int,
nombre varchar (50),
estado varchar (1),
PRIMARY KEY (id),
FOREIGN KEY (id_categorias) REFERENCES categorias (id));


CREATE TABLE compras (
id int AUTO_INCREMENT NOT NULL,
id_pagos int ,
id_producto int,
id_cliente int,
fecha date,
estado varchar (1),
PRIMARY KEY (id),
FOREIGN KEY (id_pagos) REFERENCES pagos (id),
FOREIGN KEY (id_producto) REFERENCES productos (id),
FOREIGN KEY (id_cliente) REFERENCES clientes (id)
);