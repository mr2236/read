from django.contrib import admin
from django.urls import path
from medium.pacotes.views import index, details, inscricao

urlpatterns = [    
    path('', index, name ='index'),    
    path('<int:pk>', details, name ='details'),    
    path('inscricao/<int:pk>', inscricao, name ='inscricao'),         
]
