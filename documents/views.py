from django.shortcuts import render, redirect
from documents.consume import postInformation, getInformation
from .models import Archivo

# Create your views here.
def myDocuments(request):

    usuario = postInformation('login', {"username" : request.user.username, "password" : request.user.username})

    if usuario['data']['rol'] == "admin":
        return redirect('/admins/')

    userId = str(usuario['data']['id'])
    products = getInformation('documents/' + userId, {}, {"authorization" : usuario['tokenSession']})
    archivos = list(Archivo.objects.values())

    return render(request, 'myDocuments.html', {
        "products" : products, 
        "usuario": usuario,
        "archivos": archivos
        })