from django.shortcuts import render
from urllib.request import urlopen
import json
from documents.consume import postInformation, getInformation

# Create your views here.
def home(request):

    usuario = postInformation('/login', {"username" : request.user.username, "password" : request.user.password})
    request.user.tokenSession = usuario.tokenSession

    products = getInformation('/documents', {}, {"authorization" : usuario.tokenSession})

    return render(request, 'products.html', {"products" : products})

def orders(request):

    esCompra = True
    if request.method == 'POST':
        if request.POST.get('btn') == 'True':
            orders = getInformation('/rents', {}, {"authorization" : request.user.tokenSession})
            esCompra = False
        else:
            orders = getInformation('/purchases', {}, {"authorization" : request.user.tokenSession})
            esCompra = True
    
    total = 0
    for order in orders:
        total += order.total

    return render(request, 'history.html', {"orders" : orders, "esCompra" : esCompra, "total": total, "quantity": len(orders) })