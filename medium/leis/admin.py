from django.contrib import admin
from .models import Lei, Artigo



class LeiAdmin(admin.ModelAdmin): #classe para customizar o admin
    list_display = ['name','slug','created_at'] #campos listados no admin
    search_fields = ['name', 'slug'] #exibe campo de pesquida no admin
    prepopulated_fields = {'slug': ('name',)}

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['artigo','lei']
    search_fields = ['artigo'] 
    list_filter = ['created_at'] #filtragem lateral

admin.site.register(Lei, LeiAdmin)
admin.site.register(Artigo, ArtigoAdmin)
