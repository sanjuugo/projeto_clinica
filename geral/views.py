from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse

def login(request):
    
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            #return HttpResponse('Autenticou')
            return render(
                        request,
                        'geral/home.html'
                    )
        else:
            #return HttpResponse('Não Autenticou')
            return redirect('login')
    return render(
        request,
        'geral/login.html'
    )
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(
        request,
        'geral/home.html'
    )