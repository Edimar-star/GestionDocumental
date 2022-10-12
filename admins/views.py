from django.shortcuts import render
from documents.consume import getInformation

# Create your views here.
def admins(request):

    tipoDocumentos = getInformation('/documentTypes', {}, {"authorization" : request.user.tokenSession})
    documents = getInformation('/documents', {}, {"authorization" : request.user.tokenSession})
    documentSelected = documents[0]
    selected = tipoDocumentos[0]

    return render(request, 'admin.html', {
        "tipoDocumentos": tipoDocumentos,
        "documents" : documents,
        "documentSelected": documentSelected,
        "selected": selected
        })