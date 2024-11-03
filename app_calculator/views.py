# views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from .calculations import (
    calcular_pilar,
    calcular_viga,
    calcular_laje,
    calcular_arco,
    calcular_trelica,
    calcular_viga_continua,
    calcular_flecha,
    calcular_detalhamento,
    calcular_fundacao
)
from .helpers import obter_estrutura_completa, gerar_relatorio_pdf

# View para a página inicial
def index(request):
    return render(request, 'index.html')

# View para calcular Pilar
@csrf_exempt
def calcular_pilar_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_pilar(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Viga
@csrf_exempt
def calcular_viga_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_viga(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Laje
@csrf_exempt
def calcular_laje_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_laje(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Arco
@csrf_exempt
def calcular_arco_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_arco(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Treliça
@csrf_exempt
def calcular_trelica_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_trelica(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Viga Contínua
@csrf_exempt
def calcular_viga_continua_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_viga_continua(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Flecha
@csrf_exempt
def calcular_flecha_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_flecha(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Detalhamento
@csrf_exempt
def calcular_detalhamento_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_detalhamento(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para calcular Fundação
@csrf_exempt
def calcular_fundacao_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_fundacao(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para retornar a estrutura completa dos campos
def estrutura_completa_view(request):
    if request.method == 'GET':
        try:
            estrutura = obter_estrutura_completa()
            return JsonResponse(estrutura)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para exportar relatório em PDF
@csrf_exempt
def exportar_relatorio_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            # Gera o relatório em PDF
            nome_arquivo = gerar_relatorio_pdf(dados)

            # Abre o arquivo gerado e retorna como resposta HTTP
            with open(nome_arquivo, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}"'
                return response
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para a página "Sobre"
def about(request):
    return render(request, 'about.html')
