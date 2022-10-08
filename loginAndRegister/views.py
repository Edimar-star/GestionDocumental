from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'signUp.html', {"form": form})