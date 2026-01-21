from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Patient
from django.core.paginator import Paginator

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
    dados = Patient.objects.all()
    page = Paginator(dados,5)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    return render(
        request,
        'geral/home.html', {'dados':page_obj  }
    )

@login_required(login_url='login')
def register(request):
    if request.method   == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        cpf = request.POST['cpf']
        birth = request.POST['birth']
        sex = request.POST['sex']

        cont = Patient(name=name, cpf=cpf, birth=birth, sex=sex, phone=phone, email=email)
        cont.save()
        return redirect('home')

    return render(  
        request,
        'geral/register.html'
    )