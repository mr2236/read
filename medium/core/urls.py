
from django.contrib import admin
from django.urls import path
from medium.core.views import home, contato

urlpatterns = [
    path('', home, name ='home'),
    path('contato/', contato, name ='contato'),    
]
