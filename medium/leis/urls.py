
from django.contrib import admin
from django.urls import path
from medium.leis.views import index, details, marcacao, marcacao_nota, voto

urlpatterns = [    
    path('', index, name ='index'),    
    path('<int:pk>', details, name ='details'),    
    path('marcacao/<int:lei>/<int:artigo>/<int:usuario>/<int:is_marcado>', marcacao, name ='marcacao'),   
    path('marcacao-nota/<int:lei>/<int:artigo>/<int:usuario>/<str:comentario>', marcacao_nota, name ='marcacao_nota'),   
    path('voto/<int:lei>/<int:artigo>/<int:usuario>/<int:tipo_voto>', voto, name ='voto'),   
]
