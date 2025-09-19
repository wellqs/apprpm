# relatorios/urls.py

from django.urls import path
# Garanta que todas as views estão sendo importadas
from .views import home_view, login_view, logout_view, gerar_pdf_view, historico_view

urlpatterns = [
    path('', home_view, name='home'),
    path('historico/', historico_view, name='historico'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'), # Esta é a linha que estava faltando ou incorreta
    path('gerar-pdf/', gerar_pdf_view, name='gerar_pdf'),
]