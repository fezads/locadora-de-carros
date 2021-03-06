from django.db import models
from Apps.Marcas import models as marca_models

# Create your models here.

class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(marca_models.Marca, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        texto = '{0} {1}'
        return texto.format(self.marca.nome, self.nome)