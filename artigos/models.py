from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artigo(models.Model):
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Artigo de {self.autor.username}"