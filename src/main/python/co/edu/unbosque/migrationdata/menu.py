import requests
import json
import src.main.python.co.edu.unbosque.textclassification.data_text as data_text


def menuEntrada():
    opcion = input("Ingrese la opcion que desea realizar: "
                   "\n1. Añadir datos"
                   "\n2. Mostrar datos \n")
    if opcion == "1":
        menuAnnadir()
    elif opcion == "2":
        opciones(menu())


def menuAnnadir():
    opcion = input("Ingrese la opcion que desea realizar: "
                   "\n1. Añadir categoria"
                   "\n2. Añadir producto"
                   "\n3. Añadir venta"
                   "\n4. Añadir ubicacion"
                   "\n5. Añadir temporada"
                   "\n6. Añadir Publicaciones"
                   "\n7. Salir\n")
    if opcion == "1":
        añadirCategoria()
    elif opcion == "2":
        añadirProducto()
    elif opcion == "3":
        añadirVentas()
    elif opcion == "4":
        añadirUbicacion()
    elif opcion == "5":
        añadirTemporada()
    elif opcion == "6":
        añadirPublicaciones()
    elif opcion == "7":
        print("Saliendo...")
    else:
        print("Opcion no valida")


def opciones(opcion):
    if opcion == "1":
        response = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/categorias")
        print(response.text)
    elif opcion == "2":
        response = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/productos")
        print(response.text)
    elif opcion == "3":
        response = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/ventas")
        print(response.text)
    elif opcion == "4":
        response = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/ubicaciones")
        print(response.text)
    elif opcion == "5":
        response = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/temporadas")
        print(response.text)
    elif opcion == "6":
        mostrarDatosPublicaciones()
    else:
        print("Opcion no valida")


def añadirCategoria():
    categoria = input("Ingrese el nombre de la categoria: ")

    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/categorias"
    data = {
        "id": "",
        "nombre": categoria,
        "estado": "A"
    }
    response = requests.post(url, json=data)
    print(response.text)
    print("entro")


def eliminarCategoria(id):
    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/categorias"
    data = {
        "id": id,
    }
    response = requests.delete(url, json=data)
    print(response.text)
    print("entro")


def añadirProducto():
    producto = input("Ingrese el nombre del producto: ")
    color = input("Ingrese el nombre del color: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    precio = input("Ingrese el precio del producto: ")

    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/productos"
    data = {
        "id": "",
        "nombre": producto,
        "cantidad": cantidad,
        "color": color,
        "precio": precio,
        "estado": "A"
    }
    response = requests.post(url, json=data)
    print(response.text)


def añadirVentas():
    producto = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la id de la categoria ")
    temporada = input("Ingrese el id de la temporada: ")
    ubicacion = input("Ingrese el id de la ubicacion: ")
    calificacion = input("Ingrese la calificacion del producto: ")

    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/ventas"
    data = {
        "id": "",
        "id_categoria": categoria,
        "id_ubicacion": ubicacion,
        "id_temporada": temporada,
        "id_producto": producto,
        "calificacion": calificacion,
        "estado": "A"
    }
    response = requests.post(url, json=data)
    print(response.text)


def añadirUbicacion():
    departamento = input("Ingrese el nombre del departamento: ")
    ciudad = input("Ingrese el nombre de la ciudad: ")

    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/ubicaciones"
    data = {
        "id": "",
        "nombre_departamento": departamento,
        "nombre_ciudad": ciudad,
        "estado": "A"
    }
    response = requests.post(url, json=data)
    print(response.text)


def añadirTemporada():
    temporada = input("Ingrese el nombre de la temporada: ")
    fecha = input("Ingrese la fecha de la temporada ej:2020-01-01: ")

    url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/temporadas"
    data = {
        "id": "",
        "nombre": temporada,
        "fecha": fecha,
        "estado": "A"
    }
    response = requests.post(url, json=data)
    print(response.text)


def añadirPublicaciones():
    url = "C:/Users/migue/PycharmProjects/BD-2-data-warehouses/src/resource/doc/fb_emp.xlsx"
    try:
        list = data_text.run(url)['datos']
        print("Cargando datos...")
        for dato in list:
            json = {
                "id": "",
                "producto": dato["product"],
                "text": dato["text"],
                "likes": dato["likes"],
                "comments": dato["comments"],
                "shares": dato["shares"],
                "calificacion": dato["value"],
                "estado": "A"
            }
            requests.post(
                'https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1'
                '/publicaciones',
                data=json)
        print("Datos cargados")
    except Exception as e:
        print(e)


def menu():
    opcion = input("Por favor seleccione una opción: "
                   "\n1. Mostrar datos de categoria"
                   "\n2. Mostrar datos de productos"
                   "\n3. Mostrar datos de ventas"
                   "\n4. Mostrar datos de ubicacion"
                   "\n5. Mostrar datos de temporada"
                   "\n6. Mostrar datos de publicaciones"
                   "\n_______________________________________\n")
    return opcion


def mostrarDatosPublicaciones():
    try:
        responses = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1"
            "/publicaciones")
        returnItems = json.loads(responses.text)["items"]
        print(returnItems)
    except Exception as e:
        print(e)
