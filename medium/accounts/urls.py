
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from medium.accounts.views import register
from django.contrib.auth.views import LogoutView
from medium.accounts.views import dashboard, editar,editar_password,password_reset,password_reset_confirm, listar_leis




urlpatterns = [    
    path('dashboard/', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>/', password_reset_confirm, name='password_reset_confirm'),
    path('editar/', editar, name='editar'),
    path('editar-senha/', editar_password, name='editar_password'),
    path('listar-leis/<int:pk>', listar_leis, name='listar_leis'),
  ]
#path('confirme-nova-senha/<str:key>



