from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('api/calcular/', views.calcular, name='calcular'),  # Rota para enviar dados de cálculo
    path('api/estrutura-completa/', views.estrutura_completa, name='estrutura_completa'),  # Rota para enviar a estrutura completa dos campos
    path('about/', views.about, name='about'),  # Exemplo de outra rota
]
