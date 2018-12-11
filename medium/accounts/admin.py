from django.contrib import admin
from .models import User



class accountsAdmin(admin.ModelAdmin): #classe para customizar o admin
    list_display = ['name','username','email','date_joined'] #campos listados no admin
    search_fields = ['name', 'email'] #exibe campo de pesquida no admin
    #prepopulated_fields = {'slug': ('name',)}



admin.site.register(User)
