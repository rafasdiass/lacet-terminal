# views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import json
from .helpers import calcular_pre_dimensionamento, obter_estrutura_completa

# View para a página inicial
def index(request):
    return render(request, 'index.html')

# View para retornar dados de cálculo em formato JSON
@csrf_exempt  # Apenas para desenvolvimento; em produção, configure o CSRF corretamente
def calcular(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            resultado = calcular_pre_dimensionamento(dados)
            return JsonResponse(resultado)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)

# View para enviar a estrutura completa dos campos
def estrutura_completa(request):
    if request.method == 'GET':
        estrutura = obter_estrutura_completa()
        return JsonResponse(estrutura)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)
def exportar_relatorio(request):
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
