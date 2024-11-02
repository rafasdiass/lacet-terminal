from django.http import JsonResponse
from django.shortcuts import render
from .models import *  # Importe os modelos que você usará
from .helpers import calcular_pre_dimensionamento, obter_estrutura_completa

# View para a página inicial
def index(request):
    return render(request, 'index.html')

# View para retornar dados de cálculo em formato JSON
def calcular(request):
    if request.method == 'POST':
        # Lógica para processar dados recebidos e retornar um cálculo
        dados = request.POST  # Substitua por processamento adequado
        resultado = calcular_pre_dimensionamento(dados)
        return JsonResponse({'resultado': resultado})

# View para enviar a estrutura completa dos campos
def estrutura_completa(request):
    if request.method == 'GET':
        estrutura = obter_estrutura_completa()  # Implemente essa função para retornar a estrutura completa
        return JsonResponse({'estrutura': estrutura})

# Exemplo de uma segunda view para a página "Sobre"
def about(request):
    return render(request, 'about.html')
