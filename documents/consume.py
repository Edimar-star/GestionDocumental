import requests
import json

URL_HOST = 'https://apirest-production-ce4b.up.railway.app/'

def getInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.get(url, json=args, headers=headers)
    data = response.json()

    return data

def postInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.post(url, json=args, headers=headers)
    data = response.json()

    return data

def deleteInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.delete(url, json=args, headers=headers)
    data = response.json()

    return data

def putInformation(name, args, headers={}):
    url = URL_HOST + name
    response = requests.put(url, json=args, headers=headers)
    data = response.json()

    return data

"""
name = "login"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOjEsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjY1NTQ4MzMwLCJleHAiOjE2NjU1NTU1MzB9.204eNJ26PZCSomE-en_Ii1UjzVMHzOaocT9NVt-dstE"
data = postInformation(name, {"username": "Edilberto", "password" : "Edimarod2001"}, {"authorization" : token})
print(data)
"""