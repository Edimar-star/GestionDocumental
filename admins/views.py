from django.shortcuts import render, redirect
from documents.consume import getInformation, putInformation, deleteInformation, postInformation
from documents.models import Archivo

# Create your views here.
def admins(request):

    usuario = postInformation('login', {"username" : request.user.username, "password" : request.user.username})

    if usuario['data']['rol'] == "user":
        return redirect('/')

    orders = getInformation('purchases', {}, {"authorization" : usuario['tokenSession']})
    esCompra = True
    
    if request.method == 'POST':

        if request.POST.get('btn') == 'True':
            orders = getInformation('rents', {}, {"authorization" : usuario['tokenSession']})
            esCompra = False

        elif request.POST.get('btn') == 'False':
            orders = getInformation('purchases', {}, {"authorization" : usuario['tokenSession']})
            esCompra = True


        elif request.POST.get('btn') == 'btn-newDocument':
            nombreDocumento = request.POST.get('nombreDocumento')
            autor = request.POST.get('autor')
            idDocumentType = int(request.POST.get('tipoDocumento'))
            cantidad = int(request.POST.get('cantidad'))
            precio = float(request.POST.get('precio'))
            tipo = request.POST.get('tipo')
            descripcion = request.POST.get('descripcion')
            filename = request.FILES.get('file')

            data = postInformation('documents', {
                "nombre": nombreDocumento,
                "autor": autor,
                "tipoDocumento": idDocumentType,
                "cantidad": cantidad,
                "precio": precio,
                "tipo": tipo,
                "descripcion": descripcion
            }, {"authorization" : usuario['tokenSession']})

            if filename:
                archivo = Archivo()
                archivo.idDocumento = data['id']
                archivo.nombre = data['nombre']
                archivo.archivo = filename

                archivo.save()

        
        elif request.POST.get('btn') == 'btn-updateDocument':
            idDocumento = request.POST.get('idDocumento')
            nombreDocumento = request.POST.get('nombreDocumento')
            autor = request.POST.get('autor')
            idDocumentType = int(request.POST.get('tipoDocumento'))
            cantidad = int(request.POST.get('cantidad'))
            precio = float(request.POST.get('precio'))
            tipo = request.POST.get('tipo')
            descripcion = request.POST.get('descripcion')

            putInformation('documents/' + idDocumento, {
                "nombre": nombreDocumento,
                "autor": autor,
                "tipoDocumento": idDocumentType,
                "cantidad": cantidad,
                "precio": precio,
                "tipo": tipo,
                "descripcion": descripcion
            }, {"authorization" : usuario['tokenSession']})


        elif request.POST.get('btn') == 'btn-deleteDocument':
            idDocumento = request.POST.get('idDocumento')

            deleteInformation('documents/' + idDocumento, {}, {"authorization" : usuario['tokenSession']})
        
    tipoDocumentos = getInformation('documentTypes', {}, {"authorization" : usuario['tokenSession']})
    documents = getInformation('documents', {}, {"authorization" : usuario['tokenSession']})
    documentSelected = documents[0] if documents != [] else {}
    selected = tipoDocumentos[0] if tipoDocumentos != [] else {}

    return render(request, 'admin.html', {
        "tipoDocumentos": tipoDocumentos,
        "documentos" : documents,
        "documentSelected": documentSelected,
        "selected": selected,
        "orders": orders,
        "usuario": usuario,
        "esCompra": esCompra
        })