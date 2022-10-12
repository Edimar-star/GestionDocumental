import requests
import json

URL_HOST = 'https://3000-edimarstar-apirest-xh8wr0qz670.ws-us70.gitpod.io'

def getInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.get(url, params=args, headers=headers)
    print(response)
    data = response.json()

    return data

def postInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.post(url, params=args, headers=headers)
    data = response.json()

    return data

def deleteInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.delete(url, params=args, headers=headers)
    data = response.json()

    return data

def putInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.put(url, params=args, headers=headers)
    data = response.json()

    return data