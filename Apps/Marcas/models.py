from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.nome