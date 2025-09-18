# relatorios/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Especialidade(models.TextChoices):
        NSS = 'NSS', 'Núcleo de Saúde do Servidor'
        SESMT = 'SESMT', 'Segurança do Trabalho'

    especialidade = models.CharField(
        max_length=5,
        choices=Especialidade.choices,
        verbose_name="Especialidade do Usuário"
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_especialidade_display()}"