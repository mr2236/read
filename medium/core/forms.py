from django import forms


class ContatoAdmin(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    msg = forms.CharField(label="Mensagem/Dúvida", widget=forms.Textarea)

