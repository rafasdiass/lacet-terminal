import math
# Importar classes de fundação e estruturas
from .estruturas import (
    Pilar, Viga, Laje, Arco, Trelica, VigaContinua, Flecha, Detalhamento
)
from .fundacoes import (
    Sapata, SapataRigida, SapataCorrida, Bloco, Tubulao, TubulaoCeuAberto,
    TubulaoArComprimido, Estaca, EstacaHeliceContinua, Radier, Barrete
)
from .solo.solo_manager import SoloManager

def calcular_pilar(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    area = largura * altura
    tensao = carga / area if area > 0 else 0
    verificacao = "Tensão dentro dos limites aceitáveis." if tensao <= 25 else "A tensão excede a resistência do material."
    return {
        'tipo': 'Pilar',
        'largura': largura,
        'altura': altura,
        'carga': carga,
        'area_secao': area,
        'tensao_normal': tensao,
        'verificacao': verificacao
    }

def calcular_viga(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    comprimento = float(dados.get('comprimento', 0))
    if comprimento <= 0:
        return {'erro': 'Comprimento inválido para viga.'}
    
    area = largura * altura
    inercia = (largura * altura**3) / 12
    momento = (carga * comprimento) / 8
    tensao = (momento * (altura / 2)) / inercia
    verificacao = "Tensão dentro dos limites aceitáveis." if tensao <= 25 else "A tensão excede a resistência do material."
    return {
        'tipo': 'Viga',
        'largura': largura,
        'altura': altura,
        'comprimento': comprimento,
        'carga': carga,
        'area_secao': area,
        'momento_inercia': inercia,
        'momento_fletor_maximo': momento,
        'tensao_normal_maxima': tensao,
        'verificacao': verificacao
    }

def calcular_laje(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    area = largura * altura
    carregamento = carga / area
    limite_carregamento = 10.0  # Exemplo de limite de carregamento
    verificacao = "Carregamento dentro dos limites aceitáveis." if carregamento <= limite_carregamento else "Carregamento excede o limite."
    return {
        'tipo': 'Laje',
        'largura': largura,
        'altura': altura,
        'carga': carga,
        'area': area,
        'carregamento': carregamento,
        'verificacao': verificacao
    }

def calcular_arco(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    raio = float(dados.get('raio', 0))
    if raio <= 0:
        return {'erro': 'Raio inválido para arco.'}
    
    area = largura * altura
    tensao = calcular_tensao_normal(carga, area)
    comprimento_arco = 2 * math.pi * raio
    verificacao = "Tensão dentro dos limites aceitáveis." if tensao <= 25 else "A tensão excede a resistência do material."
    return {
        'tipo': 'Arco',
        'largura': largura,
        'altura': altura,
        'carga': carga,
        'raio': raio,
        'comprimento_arco': comprimento_arco,
        'area': area,
        'tensao_normal': tensao,
        'verificacao': verificacao
    }

def calcular_trelica(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    area = largura * altura
    tensao = calcular_tensao_normal(carga, area)
    verificacao = "Tensão dentro dos limites aceitáveis." if tensao <= 25 else "A tensão excede a resistência do material."
    return {
        'tipo': 'Treliça',
        'largura': largura,
        'altura': altura,
        'carga': carga,
        'area': area,
        'tensao_normal': tensao,
        'verificacao': verificacao
    }

def calcular_viga_continua(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    comprimento = float(dados.get('comprimento', 0))
    if comprimento <= 0:
        return {'erro': 'Comprimento inválido para viga contínua.'}
    
    area = largura * altura
    momento = calcular_momento_fletor(carga, comprimento)
    tensao = calcular_tensao_normal(momento, area)
    verificacao = "Tensão dentro dos limites aceitáveis." if tensao <= 25 else "A tensão excede a resistência do material."
    return {
        'tipo': 'Viga Contínua',
        'largura': largura,
        'altura': altura,
        'comprimento': comprimento,
        'carga': carga,
        'area': area,
        'momento_fletor': momento,
        'tensao_normal': tensao,
        'verificacao': verificacao
    }

def calcular_flecha(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    comprimento = float(dados.get('comprimento', 0))
    if comprimento <= 0:
        return {'erro': 'Comprimento inválido para flecha.'}
    
    deflexao = (5 * carga * comprimento**4) / (384 * 210000 * (largura * altura**3))
    return {
        'tipo': 'Flecha',
        'largura': largura,
        'altura': altura,
        'comprimento': comprimento,
        'carga': carga,
        'deflexao': deflexao,
        'verificacao': "Deflexão dentro dos limites aceitáveis." if deflexao < 0.03 * comprimento else "Deflexão excessiva."
    }

def calcular_detalhamento(dados):
    # Detalhamento específico da peça com base nas entradas fornecidas.
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    return {
        'tipo': 'Detalhamento',
        'largura': largura,
        'altura': altura,
        'carga': carga,
        'detalhe': 'Detalhamento estrutural gerado com sucesso.'
    }

def calcular_fundacao(dados):
    tipo_fundacao = dados.get('tipo_fundacao')
    carga = float(dados.get('carga', 0))
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    profundidade = float(dados.get('profundidade', 0))

    if not tipo_fundacao:
        return {'erro': 'Tipo de fundação não especificado.'}

    fundacoes = {
        'sapata': Sapata(largura, altura, carga, profundidade),
        'sapata_rigida': SapataRigida(largura, altura, carga, profundidade),
        'sapata_corrida': SapataCorrida(largura, altura, carga, profundidade),
        'bloco': Bloco(largura, altura, carga, profundidade),
        'barrete': Barrete(largura, altura, carga, profundidade),
        'estaca': Estaca(largura, altura, carga, profundidade),
        'estaca_helice_continua': EstacaHeliceContinua(largura, altura, carga, profundidade),
        'radier': Radier(largura, altura, carga, profundidade),
        'tubulao': Tubulao(largura, altura, carga, profundidade),
        'tubulao_ceu_aberto': TubulaoCeuAberto(largura, altura, carga, profundidade),
        'tubulao_ar_comprimido': TubulaoArComprimido(largura, altura, carga, profundidade)
    }

    fundacao = fundacoes.get(tipo_fundacao)
    if not fundacao:
        return {'erro': f'Tipo de fundação "{tipo_fundacao}" não reconhecido.'}

    resultado = fundacao.gerar_relatorio()
    return resultado