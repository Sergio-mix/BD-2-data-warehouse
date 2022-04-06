import src.main.python.co.edu.unbosque.textclassification.data_text as data_text
import requests
import json

# auth_data = {'email': 'juanjo@j2logo.com', 'pass': '1234'}
# resp = requests.post('https://mipagina.xyz/login/', data=auth_data)

list = data_text.run("C:/Users/migue/PycharmProjects/BD-2-data-warehouse/src/resource/doc/fb_emp.xlsx")['datos']
url = "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/publicaciones"
data = {
    "id": "",
    "text": "nd",
    "likes": 2,
    "comments": 3,
    "shares": 4,
    "calificacion": "bueno",
    "estado": "A",
    "producto": "celular"
}
response = requests.post(url, json=data)
responses = requests.get(
    "https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/publicaciones")
print(responses.text)




for i in range(len(list)):
    resp = requests.post('https://gf45e9f189895df-data1warehouse.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/data/v1/publicaciones', data=list[i])
    print(resp)