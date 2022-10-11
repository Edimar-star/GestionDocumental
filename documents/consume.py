import requests
import json

def getInformation(url, args):
    response = requests.get(url, params=args)
    print(response)
    data = response.json()

    return data

def postInformation(url, args):
    response = requests.post(url, params=args)
    data = response.json()

    return data

def deleteInformation(url, args):
    response = requests.delete(url, params=args)
    data = response.json()

    return data

def putInformation(url, args):
    response = requests.put(url, params=args)
    data = response.json()

    return data

url = 'https://3000-edimarstar-apirest-xh8wr0qz670.ws-us70.gitpod.io/prueba'
datos = getInformation(url, {"valor": "dede"})
print(datos)