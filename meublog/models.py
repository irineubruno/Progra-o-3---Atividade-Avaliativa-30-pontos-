from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset().filter(status='publicado')


class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    objects = models.Manager()
    publicados = PublicadosManager()

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    corpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meublog_posts')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')

    class Meta:
        ordering = ('-publicado',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo
    """
    def get_absolute_url(self):
        return reverse('meublog:detalhe',
                       args=[self.publicado.year,
                             self.publicado.month,
                             self.publicado.day-1,
                             self.slug])
    """

class Comentario(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField('E-mail')
    corpo = models.TextField('Comentário')
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    atualizado = models.DateTimeField('Data de atualização', default=timezone.now)
    ativo  = models.BooleanField('Ativo', default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-criado',)
        verbose_name = "Comentário"
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.nome

