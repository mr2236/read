from django.shortcuts import render
from ..leis.models import Lei
from ..pacotes.models import Pacote
from .forms import ContatoAdmin


# Create your views here.
def home(request):
    leis = Lei.objects.all()
    pacotes = Pacote.objects.all()
    template_name = 'home.html'
    context = {
        'leis': leis,
        'pacotes': pacotes,
    }
    return render(request, template_name, context)

def contato(request):
    context = {}
    if request.method =='POST':
        form = ContatoAdmin(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form = ContatoAdmin()
    else:
        form = ContatoAdmin()
    template_name='contato.html'
    
    context['form'] = form
    return render(request, template_name, context)