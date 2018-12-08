from django.db import models
from django.conf import settings


# Create your models here.

class LeiManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | 
            models.Q(description__icontains=query)
        )


class Lei(models.Model):
    name  = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank = True, null=True)

    image = models.ImageField(
        upload_to='leis/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = LeiManager() #acessar Lei.objects.search('keyword')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lei'
        verbose_name_plural = 'Leis'
        #ordering = ['name'] -- ordena a exibição dos nomes no admin

class Artigo(models.Model):
    artigo = models.TextField('Artigo/Inciso')
    id_artigo_lei = models.IntegerField('Artigo Lei', blank=True, null=True)

    lei = models.ForeignKey(Lei, on_delete=models.CASCADE, verbose_name='Lei', related_name='artigos')

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.artigo

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"        

class Marcacao(models.Model):
    lei = models.ForeignKey(Lei, on_delete=models.CASCADE, verbose_name='Lei', related_name='marcacaoArtigos')
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, verbose_name='Artigo', related_name='marcacaoLei')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='marcacaoUsuario', related_name='marcacaoUsuario')
    is_marcado = models.BooleanField('Está Marcado?', blank=True, default=False)
    description = models.TextField('Descrição', blank = True, null=True)
    is_importante = models.BooleanField('É importante?', blank=True, default=False)
    votos = models.IntegerField('Votos', blank=True, default=0)

    def __str__(self):
        return self.description


