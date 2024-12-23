# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('calcular/pilar/', views.calcular_pilar_view, name='calcular_pilar'),
    path('calcular/viga/', views.calcular_viga_view, name='calcular_viga'),
    path('calcular/laje/', views.calcular_laje_view, name='calcular_laje'),
    path('calcular/fundacao/', views.calcular_fundacao_view, name='calcular_fundacao'),
    path('calcular/arco/', views.calcular_arco_view, name='calcular_arco'),
    path('calcular/trelica/', views.calcular_trelica_view, name='calcular_trelica'),
    path('calcular/viga-continua/', views.calcular_viga_continua_view, name='calcular_viga_continua'),
    path('calcular/flecha/', views.calcular_flecha_view, name='calcular_flecha'),
    path('calcular/detalhamento/', views.calcular_detalhamento_view, name='calcular_detalhamento'),
    path('estrutura-completa/', views.estrutura_completa_view, name='estrutura_completa'),
    path('exportar-relatorio/', views.exportar_relatorio_view, name='exportar_relatorio'),
    path('materiais-disponiveis/', views.obter_materiais_view, name='materiais_disponiveis'),
    path('solos-disponiveis/', views.obter_solos_view, name='solos_disponiveis'),
]
