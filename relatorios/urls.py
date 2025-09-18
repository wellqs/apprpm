from django.urls import path
# Adicione a nova view aqui
from .views import home_view, login_view, logout_view, gerar_pdf_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Adicione esta nova linha
    path('gerar-pdf/', gerar_pdf_view, name='gerar_pdf'),
]