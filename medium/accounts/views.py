from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.conf import settings
from .forms import RegisterForm, EditarAccountForm, PasswordResetForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
#from medium.core.utils import generate_hash_key
from .models import PasswordReset
from ..pacotes.models import Inscricao, Pacote


User = get_user_model

@login_required
def dashboard(request):
    pacotes = Pacote.objects.filter(inscricao__user_id = request.user.id)       
    context = {
        'pacotes': pacotes,        
    }    
    template_name='accounts/dashboard.html'
    return render(request, template_name, context)

@login_required
def listar_leis(request, pk):
    pacotes = Pacote.objects.get(id = pk)     
    print(pacotes)  
    context = {
        'leis': pacotes.leis.all(), 
        'pacote': pacotes,
    }    
    template_name='accounts/listar_leis.html'
    return render(request, template_name, context)


@login_required
def editar(request):
    template_name='accounts/editar.html'    
    context = {}
    form = EditarAccountForm(instance=request.user)
    if request.method == 'POST':
        form = EditarAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarAccountForm(instance=request.user)
            context['success'] = True
        else:
            form = EditarAccountForm(instance=request.user)    
    context['form'] = form
    return render(request, template_name, context)


def register(request):
    template_name='accounts/register.html'
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def editar_password(request):
    template_name= 'accounts/editar_password.html'
    context = {}
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            form = PasswordChangeForm(user=request.user)    
    context['form'] = form
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)