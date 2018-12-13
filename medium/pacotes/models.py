from django.db import models
from django.conf import settings
from ..leis.models import Lei
from django import forms



class Pacote(models.Model):
    name  = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank = True, null=True)
    ativo = models.BooleanField('Está ativo?', blank = True, default= False)
    lei = models.ForeignKey(Lei, on_delete=models.CASCADE, verbose_name="Lei", related_name="lei", default=0)
    
    image = models.ImageField(
        upload_to='pacotes/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.name

class Inscricao(models.Model):

    STATUS_CHOICES=(
        (
            (0, 'Pendente'),
            (1, 'Aprovado'),
            (2, 'Cancelado'),
        )
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name="Usuário", related_name="inscricao") #inscricao é criado no usuario
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE, verbose_name="Pacote", related_name="inscricao")
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default = 0, blank=True
        )
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user','pacote'))

        