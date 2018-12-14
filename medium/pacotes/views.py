from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pacote, Inscricao
from ..accounts.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Exists, OuterRef, F, Max, Sum
from django.contrib.auth.decorators import login_required


def index(request):    
    pacotes = Pacote.objects.all()      

    template_name = 'pacotes/index.html'

    context = {
        'pacotes': pacotes,        
    }
    return render(request, template_name, context)

def details(request, pk):
    pacote = get_object_or_404(Pacote, pk=pk)    
    leis = pacote.leis.all()
    print(leis)
    
    template_name = 'pacotes/details.html'
    context = {
        'pacote': pacote,
        'leis': leis,
    }
    return render(request, template_name, context)


@login_required
def inscricao(request, pk):
  pacote = get_object_or_404(Pacote, pk=pk)    
  inscricao, created  = Inscricao.objects.get_or_create(user=request.user, pacote=pacote)
  if created:
    inscricao.active()
  return redirect('accounts:dashboard')  

    




