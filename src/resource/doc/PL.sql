DECLARE
id number;
valor int;
id_producto int;
id_cliente int;
fecha date;
forma_pago varchar (40);
estado varchar (1);

BEGIN
cantidad_comprada := 2;
id_compras := null;
valor_compra := 1200000;
id_producto := 1;
id_cliente := 1;
fecha SYSDATE;
forma_pago := 'Efectivo';
estado := 'A';
INSERT INTO COMPRAS VALUES (id_compras,valor_compra , id_producto,id_cliente, fecha ,forma_pago, estado );
UPDATE PRODUCTOS SET CANTIDAD = CANTIDAD - cantidad_comprada WHERE id_producto = 1;
  COMMIT;
EXCEPTION
  WHEN OTHERS THEN
  dbms_output.put_line('Error en la transaccion:'||SQLERRM);
  dbms_output.put_line('Se deshacen las modificaciones');
  ROLLBACK;
END;