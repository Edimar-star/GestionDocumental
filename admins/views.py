from django.shortcuts import render

# Create your views here.
def admins(request):
    return render(request, 'admin.html')