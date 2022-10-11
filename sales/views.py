from django.shortcuts import render
from urllib.request import urlopen
import json

# Create your views here.
def home(request):

    products = [
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"},
        {"id": 1, "nombre": "producto", 
        "descripcion" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 5000, "img": "https://unsplash.it/400/200", "type": "Fisico"}
    ]

    return render(request, 'products.html', {"products" : products})

def orders(request):

    esCompra = True
    if request.method == 'POST':
        if request.POST.get('btn') == 'True':
            esCompra = False
        else:
            esCompra = True

    orders = [
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"},
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"},
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"},
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"},
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"},
        {"nombre": "documento","username": "John", "cantidad": 5, "total" : 75000, "fechaInicioAlquile" : "10/10/2022", "fechaFinAlquile": "10/10/2022"}
    ]

    #url = "https://rickandmortyapi.com/api/character"
    #response = urlopen(url)
    #data = json.loads(response.read())

    #print(data)

    return render(request, 'history.html', {"orders" : orders, "esCompra" : esCompra, "total": 75000, "quantity": 5 })