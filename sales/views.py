from django.shortcuts import render, redirect
from documents.consume import postInformation, getInformation

# Create your views here.
def home(request):

    usuario = postInformation('login', {"username" : request.user.username, "password" : request.user.username})

    if usuario['data']['rol'] == "admin":
        return redirect('/admins/')

    products = getInformation('documents', {}, {"authorization" : usuario['tokenSession']})

    if request.method == "POST":
        if request.POST.get('newOrder') == "comprar":
            idDocumento = request.POST.get('idDocumento')
            idCliente = request.POST.get('idCliente')
            total = int(request.POST.get('total'))

            postInformation('purchases', {
                "idDocumento": idDocumento,
                "idCliente": idCliente,
                "total": total
            }, {"authorization" : usuario['tokenSession']})

        elif request.POST.get('newOrder') == "alquilar":
            idDocumento = request.POST.get('idDocumento')
            idCliente = request.POST.get('idCliente')
            total = int(request.POST.get('total'))

            postInformation('rents', {
                "idDocumento": idDocumento,
                "idCliente": idCliente,
                "total": total
            }, {"authorization" : usuario['tokenSession']})

    return render(request, 'products.html', {
        "products" : products, 
        "usuario": usuario
        })

def orders(request):

    usuario = postInformation('login', {"username" : request.user.username, "password" : request.user.username})

    if usuario['data']['rol'] == "admin":
        return redirect('/admins/')

    userId = str(usuario['data']['id'])
    orders = getInformation('purchases/' + userId, {}, {"authorization" : usuario['tokenSession']})
    esCompra = True
    
    if request.method == 'POST':
        if request.POST.get('btn') == 'True':
            orders = getInformation('rents/' + userId, {}, {"authorization" : usuario['tokenSession']})
            esCompra = False
        else:
            orders = getInformation('purchases/' + userId, {}, {"authorization" : usuario['tokenSession']})
            esCompra = True
    
    print(orders)
    print(userId)
    total = 0
    for order in orders:
        total += order['total']

    cantidad = len(orders)

    return render(request, 'history.html', {
        "orders" : orders, 
        "esCompra" : esCompra, 
        "total": total, 
        "quantity": cantidad, 
        "usuario": usuario
        })