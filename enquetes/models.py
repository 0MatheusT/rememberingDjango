import datetime

from django.db import models
from django.utils import timezone


class Perguntas(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("Data de Publicação")

    def __str__(self):
        return self.texto_pergunta

    def publicado_recentemente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)


class Escolhas(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)
    texto_de_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_de_escolha
