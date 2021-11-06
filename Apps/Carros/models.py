from django.db import models
from Apps.Modelos import models as modelo_models

# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.ForeignKey(modelo_models.Modelo, on_delete=models.CASCADE)
    ano = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    descricao = models.TextField(max_length=200)
    observacoes = models.TextField(max_length=200)

    def __str__(self):
        texto = '{0} {1} (Placa: {2})'
        return texto.format(self.modelo, self.ano, self.placa)