import requests
import pandas as pd
import json

URL= "https://jsonplaceholder.typicode.com/users"

repuesta = requests.get(URL)

if repuesta.status_code == 200:
    print('Solicitud exitosa')
    print('Datos: ',repuesta.json())
else:
    print('Error en la solicitud del recurso. Detalles:  \n',
           repuesta.text)

#solicitud de un recurso

URL= 'https://jsonplaceholder.typicode.com/comments?postId=1'

repuesta = requests.get(URL)

if repuesta.status_code == 200:
    print('Solicitud exitosa')
    print('Datos: ',repuesta.json())
else:
    print('Error en la solicitud del recurso. Detalles:  \n',
           repuesta.text)
    

#envio de un recurso a endpoint

URL= 'https://jsonplaceholder.typicode.com/posts'


datos={
    'title': 'Titulo de ejemplo',
    'body': 'parrafo de ejemplo',
    'id': 1

}
headres= { 
    'Content-type': 'application/json; charset=UTF-8'
}

repuesta = requests.post(URL,data=json.dumps(datos),  headers=headres)
repuesta_json = repuesta.json()
print(repuesta_json)
print(repuesta.status_code)

#Metodo delete
URL= 'https://jsonplaceholder.typicode.com/posts/101'

repuesta = requests.delete(URL)
print(repuesta.status_code)

URL = "http://127.0.0.1:5050/pedidos/CA-2016-152156"
repuesta= requests.get(URL)
print(repuesta.text)