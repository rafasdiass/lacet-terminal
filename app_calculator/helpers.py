# helpers.py

import math

# Importar classes de fundação
# Imports ajustados para o nome correto do pacote
from .fundacoes.barrete import Barrete
from .fundacoes.bloco import Bloco
from .fundacoes.estaca import Estaca
from .fundacoes.estaca_helice_continua import EstacaHeliceContinua
from .fundacoes.radier import Radier
from .fundacoes.sapata_corrida import SapataCorrida
from .fundacoes.sapata_rigida import SapataRigida
from .fundacoes.sapata import Sapata
from .fundacoes.tubulao_ar_comprimido import TubulaoArComprimido
from .fundacoes.tubulao_ceu_aberto import TubulaoCeuAberto
from .fundacoes.tubulao import Tubulao
from .solo.solo_manager import SoloManager

# Funções de cálculo matemático
def calcular_area_retangular(largura: float, altura: float) -> float:
    """Calcula a área de um retângulo."""
    return largura * altura

def calcular_area_circular(diametro: float) -> float:
    """Calcula a área de um círculo dado o diâmetro."""
    raio = diametro / 2
    return math.pi * raio ** 2

def calcular_volume_cilindrico(diametro: float, altura: float) -> float:
    """Calcula o volume de um cilindro com base no diâmetro e altura."""
    area_base = calcular_area_circular(diametro)
    return area_base * altura

def calcular_momento_fletor(carga: float, comprimento: float) -> float:
    """Calcula o momento fletor máximo para uma carga distribuída em uma viga simplesmente apoiada."""
    return (carga * comprimento) / 8

def calcular_forca_cisalhante(carga: float, comprimento: float) -> float:
    """Calcula a força de cisalhamento máxima para uma carga distribuída em uma viga."""
    return carga / 2

def calcular_tensao_normal(carga: float, area: float) -> float:
    """Calcula a tensão normal dada a carga e a área de aplicação."""
    return carga / area if area > 0 else 0

def calcular_peso_concreto(volume: float, peso_especifico: float = 25) -> float:
    """Calcula o peso do concreto, assumindo um peso específico padrão de 25 kN/m³."""
    return volume * peso_especifico

def verificar_resistencia_material(tensao_aplicada: float, resistencia_material: float) -> str:
    """Verifica se a tensão aplicada está dentro dos limites de resistência do material."""
    if tensao_aplicada > resistencia_material:
        return "A tensão excede a resistência do material. Reforço necessário."
    else:
        return "Tensão dentro dos limites aceitáveis."

def calcular_pre_dimensionamento(dados):
    """
    Função que realiza o cálculo de pré-dimensionamento
    baseado nos dados fornecidos.
    """
    # Extraia os dados necessários
    tipo_peca = dados.get('tipo_peca')
    carga = float(dados.get('carga', 0))

    # Validação básica
    if not tipo_peca or carga <= 0:
        return {'erro': 'Dados inválidos.'}

    # Lógica de cálculo baseada no tipo de peça
    calculadoras = {
        'pilar': calcular_pilar,
        'viga': calcular_viga,
        'laje': calcular_laje,
        'fundacao': calcular_fundacao,
        # Adicione outros tipos conforme necessário
    }

    calculadora = calculadoras.get(tipo_peca)

    if calculadora:
        return calculadora(dados)
    else:
        return {'erro': 'Tipo de peça não suportado.'}

def calcular_pilar(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))

    # Calcula a área da seção transversal
    area = calcular_area_retangular(largura, altura)
    # Calcula a tensão normal
    tensao = calcular_tensao_normal(carga, area)
    # Verifica resistência do material (exemplo com resistência de 25 MPa)
    resistencia = 25.0
    verificacao = verificar_resistencia_material(tensao, resistencia)
    return {
        'tipo': 'Pilar',
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
    # Calcula a área da seção transversal
    area = calcular_area_retangular(largura, altura)
    # Calcula o momento de inércia
    inercia = (largura * altura**3) / 12
    # Calcula o momento fletor máximo
    momento = calcular_momento_fletor(carga, comprimento)
    # Calcula a tensão normal máxima
    tensao = (momento * (altura / 2)) / inercia
    # Verifica resistência do material (exemplo com resistência de 25 MPa)
    resistencia = 25.0
    verificacao = verificar_resistencia_material(tensao, resistencia)
    return {
        'tipo': 'Viga',
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

    # Calcula a área da laje
    area = calcular_area_retangular(largura, altura)
    # Calcula o carregamento por unidade de área
    carregamento = carga / area
    # Verifica se o carregamento está dentro de limites aceitáveis (exemplo)
    limite_carregamento = 10.0  # kN/m²
    if carregamento > limite_carregamento:
        verificacao = "Carregamento excede o limite. Reforço necessário."
    else:
        verificacao = "Carregamento dentro dos limites aceitáveis."
    return {
        'tipo': 'Laje',
        'area': area,
        'carregamento': carregamento,
        'verificacao': verificacao
    }

def calcular_fundacao(dados):
    tipo_fundacao = dados.get('tipo_fundacao')
    solo_tipo = dados.get('solo_tipo')
    profundidade = float(dados.get('profundidade', 0))
    carga = float(dados.get('carga', 0))
    kwargs = dados.copy()
    kwargs.pop('tipo_peca', None)
    kwargs.pop('tipo_fundacao', None)
    kwargs.pop('solo_tipo', None)
    kwargs.pop('profundidade', None)
    kwargs.pop('carga', None)

    if not tipo_fundacao:
        return {'erro': 'Tipo de fundação não especificado.'}

    try:
        fundacao = FundacaoManager.criar_fundacao(
            tipo=tipo_fundacao,
            solo_tipo=solo_tipo,
            profundidade=profundidade,
            carga=carga,
            **kwargs
        )
        resultado = fundacao.gerar_relatorio()  # Supondo que cada classe de fundação tenha um método gerar_relatorio()
        return resultado
    except Exception as e:
        return {'erro': str(e)}

class FundacaoManager:
    @staticmethod
    def criar_fundacao(tipo, solo_tipo=None, profundidade=None, carga=0, **kwargs):
        # Se o tipo de solo foi fornecido, cria uma camada de solo com o SoloManager
        solo = None
        if solo_tipo and profundidade:
            solo = SoloManager.criar_camada(solo_tipo, profundidade)

        # Inicializa a fundação com os dados de solo se disponíveis
        if tipo == "barrete":
            return Barrete(solo=solo, carga=carga, **kwargs)
        elif tipo == "bloco":
            return Bloco(solo=solo, carga=carga, **kwargs)
        elif tipo == "estaca":
            return Estaca(solo=solo, carga=carga, **kwargs)
        elif tipo == "estaca_helice_continua":
            return EstacaHeliceContinua(solo=solo, carga=carga, **kwargs)
        elif tipo == "radier":
            return Radier(solo=solo, carga=carga, **kwargs)
        elif tipo == "sapata_corrida":
            return SapataCorrida(solo=solo, carga=carga, **kwargs)
        elif tipo == "sapata_rigida":
            return SapataRigida(solo=solo, carga=carga, **kwargs)
        elif tipo == "sapata":
            return Sapata(solo=solo, carga=carga, **kwargs)
        elif tipo == "tubulao_ar_comprimido":
            return TubulaoArComprimido(solo=solo, carga=carga, **kwargs)
        elif tipo == "tubulao_ceu_aberto":
            return TubulaoCeuAberto(solo=solo, carga=carga, **kwargs)
        elif tipo == "tubulao":
            return Tubulao(solo=solo, carga=carga, **kwargs)
        else:
            raise ValueError(f"Tipo de fundação '{tipo}' não reconhecido.")

def obter_estrutura_completa():
    """
    Retorna a estrutura completa dos campos necessários para cada tipo de peça.
    """
    estrutura = {
        'pilar': {
            'campos': [
                {'nome': 'largura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Largura do pilar em metros'},
                {'nome': 'altura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Altura do pilar em metros'},
                {'nome': 'carga', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Carga aplicada em kN'},
            ],
            'metadados': {'descricao': 'Cálculo de pré-dimensionamento de pilar'},
        },
        'viga': {
            'campos': [
                {'nome': 'largura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Largura da viga em metros'},
                {'nome': 'altura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Altura da viga em metros'},
                {'nome': 'carga', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Carga aplicada em kN'},
                {'nome': 'comprimento', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Comprimento da viga em metros'},
            ],
            'metadados': {'descricao': 'Cálculo de pré-dimensionamento de viga'},
        },
        'laje': {
            'campos': [
                {'nome': 'largura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Largura da laje em metros'},
                {'nome': 'altura', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Espessura da laje em metros'},
                {'nome': 'carga', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Carga aplicada em kN'},
            ],
            'metadados': {'descricao': 'Cálculo de pré-dimensionamento de laje'},
        },
        'fundacao': {
            'campos': [
                {'nome': 'tipo_fundacao', 'tipo': 'string', 'obrigatorio': True, 'opcoes': ['sapata', 'estaca', 'bloco', 'barrete', 'radier', 'tubulao'], 'descricao': 'Tipo de fundação'},
                {'nome': 'solo_tipo', 'tipo': 'string', 'obrigatorio': True, 'opcoes': ['arenoso', 'argiloso', 'rochoso'], 'descricao': 'Tipo de solo'},
                {'nome': 'profundidade', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Profundidade em metros'},
                {'nome': 'carga', 'tipo': 'float', 'obrigatorio': True, 'descricao': 'Carga aplicada em kN'},
                # Adicione outros campos específicos de acordo com o tipo de fundação
            ],
            'metadados': {'descricao': 'Cálculo de pré-dimensionamento de fundação'},
        },
        # Adicione outros tipos de peças conforme necessário
    }
    return estrutura
