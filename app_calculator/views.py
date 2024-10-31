from django.shortcuts import render
from django.http import HttpResponse

# View para a página inicial
def index(request):
    return render(request, 'index.html')

# Exemplo de uma segunda view para a página "Sobre"
def about(request):
    return render(request, 'about.html')
