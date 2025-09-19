# relatorios/models.py

from django.db import models
from zoneinfo import ZoneInfo
from django.contrib.auth.models import User

# --- CLASSE PROFILE (INDEPENDENTE) ---
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


# --- CLASSE RELATORIO (INDEPENDENTE E DEFINIDA APENAS UMA VEZ) ---
class Relatorio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relatorios')
    especialidade = models.CharField(max_length=5)
    report_html = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_criacao']  # Ordena do mais novo para o mais antigo

    def __str__(self):
        data_local = self.data_criacao.astimezone(ZoneInfo("America/Porto_Velho"))
        return f"Relatório de {self.usuario.username} em {data_local.strftime('%d/%m/%Y %H:%M')}"