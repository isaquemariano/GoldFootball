from django.db import models


class jogadores(models.Model):
    nome = models.CharField(max_length=30)
    posicao = models.CharField(max_length=20)
    numero = models.CharField(max_length=2)