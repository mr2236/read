from django import forms
from django.core.mail import send_mail
from django.conf import settings
from medium.core.mail import send_mail_template
#from medium.leis.views import index, details, marcacao, marcacao_nota, voto



class ContatoAdmin(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem/Dúvida", widget=forms.Textarea)

    def send_mail(self):
        subject = 'Contato do site Lei-e'
        #message = 'Nome: %(name)s;E-mail: %(email)s;%(message)s '
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        #message = message % context
        template_name = 'contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
