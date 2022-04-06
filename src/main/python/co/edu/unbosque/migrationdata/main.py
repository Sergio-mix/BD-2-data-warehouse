import src.main.python.co.edu.unbosque.textclassification.data_text as data_text
import requests
import json


def cargarDatos(url):
    try:
        list = data_text.run(url)['datos']
        print("Cargando...")
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


def mostrarDatos():
    try:
        responses = requests.get(
            "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1"
            "/publicaciones")
        returnItems = json.loads(responses.text)["items"]
        print(returnItems)
    except Exception as e:
        print(e)


cargarDatos("C:/Users/alejo/IdeaProjects/bd-2 data warehouse/src/resource/doc/fb_emp.xlsx")
