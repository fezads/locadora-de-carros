from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        texto = '{0} - {1}'
        return texto.format(self.cpf, self.nome)