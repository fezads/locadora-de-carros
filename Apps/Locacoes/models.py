from django.db import models
from Apps.Carros import models as carro_models
from Apps.Clientes import models as cliente_models

# Create your models here.

class Locacao(models.Model):
    carro = models.ForeignKey(carro_models.Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente_models.Cliente, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    valor = models.CharField(max_length=50)
    observacoes = models.CharField(max_length=200)

    def __str__(self):
        return self.nome