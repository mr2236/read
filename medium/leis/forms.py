from django import forms
from .models import Marcacao

class ContatoAdmin(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    msg = forms.CharField(label="Mensagem/Dúvida", widget=forms.Textarea)

class MarcacaoForm(forms.ModelForm):

    class Meta:
        model = Marcacao                
        fields = ['lei','artigo', 'usuario', 'description', 'is_marcado' ]

 