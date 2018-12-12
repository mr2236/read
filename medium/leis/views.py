from django.shortcuts import render, get_object_or_404
from .models import Lei, Artigo, Marcacao
from ..accounts.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import MarcacaoForm
from django.db.models import Exists, OuterRef, F, Max, Sum


def index(request):
    leis = {}

    leis_all = Lei.objects.all()    
    if request.user.is_authenticated:
        user = User.objects.get(id= request.user.id)    
        leis = Lei.objects.filter( marcacaoArtigos__usuario= user ).distinct()

    template_name = 'leis/index.html'
    context = {
        'leis': leis,
        'leis_all': leis_all
    }
    return render(request, template_name, context)


#retorna artigos da lei pk
def details(request, pk):
    lei = get_object_or_404(Lei, pk=pk)    
    artigos = Artigo.objects.filter(lei=pk)    
    artigos = (
    Artigo
    .objects
    .filter(lei=pk)
    .annotate(
        is_marcado=Exists(
            Marcacao
            .objects
            .filter(
                artigo_id=OuterRef('id'),
                usuario=request.user,
                is_marcado=1,
            )
           )
        )
    .annotate(
        description=(F('marcacaoLei__description'))    
    ).annotate(
        votos=(F('marcacaoLei__votos'))
    )      
    ).order_by('id')
    print(artigos.query)
    
    context = {
        'artigos': artigos,
        'lei': lei,        
    }
  
    template_name = 'leis/details.html'
    return render(request, template_name, context)

@csrf_exempt
def marcacao(request, lei, artigo, usuario, is_marcado):    
    form = MarcacaoForm(request.POST)        
    if request.is_ajax():
        if request.method == 'POST':
            print (usuario)   
            print (lei)   
            print (artigo)  
            print (is_marcado)            
            if form.is_valid(): 
                marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(is_marcado=is_marcado)  
                if not marcacao:    
                   form.save() 
                # else:
                #    marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario)
                #    marcacao.delete()
            else:
                print(form.errors)
                form = MarcacaoForm()
    return JsonResponse({'lei': lei })


@csrf_exempt
def marcacao_nota(request, lei, artigo, usuario, comentario):    
    form = MarcacaoForm(request.POST)        
    if request.is_ajax():
        if request.method == 'POST':
            print (usuario)   
            print (lei)   
            print (artigo)  
            print (comentario)            
            if form.is_valid():     
                if comentario == "comentario_delete":
                    comentario = ""
                marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(description=comentario)         
                print(marcacao)   
                if not marcacao:          
                    form.save()   
                    marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(description=comentario)         
            else:
                print(form.errors)
                form = MarcacaoForm()
    return JsonResponse({'comentario': comentario })

@csrf_exempt
def voto(request, lei, artigo, usuario, tipo_voto):    
    form = MarcacaoForm(request.POST)   
    context = {}     
    if request.is_ajax():
        if request.method == 'POST':                    
            if form.is_valid():
                    if tipo_voto == 1:                   
                        marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(votos=F('votos')+1)                             
                    else:
                        marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(votos=F('votos')-1)                             
                    if not marcacao:
                        form.save()                           
                        if tipo_voto == 1:                   
                            marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(votos=1)                             
                        else:
                            marcacao = Marcacao.objects.filter(artigo_id=artigo, lei_id=lei, usuario_id=usuario).update(votos=-1)   
                    voto = Marcacao.objects.get(artigo_id=artigo, lei_id=lei, usuario_id=usuario).votos                   
                    context = {
                        'voto': voto,        
                    }
            else:
                print(form.errors)
                form = MarcacaoForm()
    
    return JsonResponse(context)
