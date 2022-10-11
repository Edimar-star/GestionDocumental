from django.shortcuts import render

# Create your views here.
def admins(request):

    tipoDocumentos = [
        {"nombre": "Edilberto"},
        {"nombre": "Mario"},
        {"nombre": "Rodriguez"},
        {"nombre": "Fontalvo"}
    ]

    return render(request, 'admin.html', {"tipoDocumentos": tipoDocumentos, "selected": tipoDocumentos[0]})