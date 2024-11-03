from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/calcular/', views.calcular, name='calcular'),
    path('api/estrutura-completa/', views.estrutura_completa, name='estrutura_completa'),
    path('api/exportar-relatorio/', views.exportar_relatorio, name='exportar_relatorio'),  # Nova rota para exportar relatório
    path('about/', views.about, name='about'),
]
