from django.shortcuts import render

# Create your views here.
def home(request):

    categories = [
        'libro electronico',
        'revista',
        'iconografico',
        'monografia',
        'ensayo',
        'investigacion'
    ]

    return render(request, 'index.html', {"categories": categories})

def document(request):
    return render(request, 'document.html')