# helpers.py

import datetime
import os

# Importar bibliotecas necessárias para geração de PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Importar classes de estruturas
from .estruturas import (
    Pilar,
    Viga,
    Laje,
    Arco,
    Trelica,
    VigaContinua,
    Flecha,
    Detalhamento
)

# Importar o FundacaoManager e SoloManager
from .fundacoes.fundacao_manager import FundacaoManager
from .solo.solo_manager import SoloManager

# Definição das opções disponíveis para campos não numéricos
MATERIAIS_DISPONIVEIS = [
    {'codigo': 'concreto_c20', 'nome': 'Concreto C20', 'resistencia': 20, 'densidade': 2400, 'modulo_elasticidade': 21000},
    {'codigo': 'concreto_c25', 'nome': 'Concreto C25', 'resistencia': 25, 'densidade': 2400, 'modulo_elasticidade': 25000},
    {'codigo': 'aco_a36', 'nome': 'Aço A36', 'resistencia': 36, 'densidade': 7850, 'modulo_elasticidade': 200000},
    # Adicione outros materiais conforme necessário
]

SOLOS_DISPONIVEIS = [
    {'codigo': 'arenoso', 'nome': 'Solo Arenoso', 'capacidade_carga': 150, 'coeficiente_atrito': 0.5, 'compressibilidade': 1.2},
    {'codigo': 'argiloso', 'nome': 'Solo Argiloso', 'capacidade_carga': 100, 'coeficiente_atrito': 0.3, 'compressibilidade': 1.5},
    {'codigo': 'rochoso', 'nome': 'Solo Rochoso', 'capacidade_carga': 300, 'coeficiente_atrito': 0.7, 'compressibilidade': 0.8},
    # Adicione outros tipos de solo conforme necessário
]

# Funções para obter as opções disponíveis
def obter_materiais_disponiveis():
    return MATERIAIS_DISPONIVEIS

def obter_solos_disponiveis():
    return SOLOS_DISPONIVEIS

def obter_todas_opcoes():
    return {
        'materiais': MATERIAIS_DISPONIVEIS,
        'solos': SOLOS_DISPONIVEIS,
        # Inclua outras opções conforme necessário
    }

# Funções de cálculo

def calcular_pilar(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    carga = float(dados.get('carga', 0))
    material_codigo = dados.get('material')

    # Validar entradas
    if largura <= 0 or altura <= 0 or carga <= 0:
        return {'erro': 'Largura, altura e carga devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Pilar e realizar o cálculo usando a classe Pilar
    pilar = Pilar(largura=largura, altura=altura, carga=carga, material=material_data)
    resultado = pilar.gerar_relatorio()

    return resultado

def calcular_viga(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    comprimento = float(dados.get('comprimento', 0))
    carga = float(dados.get('carga', 0))
    material_codigo = dados.get('material')
    tipo_carga = dados.get('tipo_carga')
    tipo_apoio = dados.get('tipo_apoio')

    # Validar entradas
    if largura <= 0 or altura <= 0 or comprimento <= 0 or carga <= 0:
        return {'erro': 'Todos os valores numéricos devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}
    if not tipo_carga:
        return {'erro': 'Tipo de carga não especificado.'}
    if not tipo_apoio:
        return {'erro': 'Tipo de apoio não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Viga e realizar o cálculo usando a classe Viga
    viga = Viga(
        largura=largura,
        altura=altura,
        comprimento=comprimento,
        carga=carga,
        material=material_data,
        tipo_carga=tipo_carga,
        tipo_apoio=tipo_apoio
    )
    resultado = viga.gerar_relatorio()

    return resultado

def calcular_laje(dados):
    largura = float(dados.get('largura', 0))
    comprimento = float(dados.get('comprimento', 0))
    carga = float(dados.get('carga', 0))
    material_codigo = dados.get('material')

    # Validar entradas
    if largura <= 0 or comprimento <= 0 or carga <= 0:
        return {'erro': 'Largura, comprimento e carga devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Laje e realizar o cálculo
    laje = Laje(largura=largura, comprimento=comprimento, carga=carga, material=material_data)
    resultado = laje.gerar_relatorio()

    return resultado

def calcular_arco(dados):
    largura = float(dados.get('largura', 0))
    espessura = float(dados.get('espessura', 0))
    raio = float(dados.get('raio', 0))
    carga = float(dados.get('carga', 0))
    material_codigo = dados.get('material')

    # Validar entradas
    if largura <= 0 or espessura <= 0 or raio <= 0 or carga <= 0:
        return {'erro': 'Todos os valores numéricos devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Arco e realizar o cálculo
    arco = Arco(
        largura=largura,
        espessura=espessura,
        raio=raio,
        carga=carga,
        material=material_data
    )
    resultado = arco.gerar_relatorio()

    return resultado

def calcular_trelica(dados):
    carga = float(dados.get('carga', 0))
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    material_codigo = dados.get('material')

    # Validar entradas
    if carga <= 0 or largura <= 0 or altura <= 0:
        return {'erro': 'Todos os valores numéricos devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Trelica e realizar o cálculo
    trelica = Trelica(
        carga=carga,
        largura=largura,
        altura=altura,
        material=material_data
    )
    resultado = trelica.gerar_relatorio()

    return resultado

def calcular_viga_continua(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    comprimento_total = float(dados.get('comprimento_total', 0))
    numero_apoios = int(dados.get('numero_apoios', 0))
    carga_distribuida = float(dados.get('carga_distribuida', 0))
    material_codigo = dados.get('material')

    # Validar entradas
    if largura <= 0 or altura <= 0 or comprimento_total <= 0 or carga_distribuida <= 0 or numero_apoios <= 1:
        return {'erro': 'Todos os valores numéricos devem ser maiores que zero e número de apoios deve ser maior que 1.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto VigaContinua e realizar o cálculo
    viga_continua = VigaContinua(
        largura=largura,
        altura=altura,
        comprimento_total=comprimento_total,
        numero_apoios=numero_apoios,
        carga_distribuida=carga_distribuida,
        material=material_data
    )
    resultado = viga_continua.gerar_relatorio()

    return resultado

def calcular_flecha(dados):
    largura = float(dados.get('largura', 0))
    altura = float(dados.get('altura', 0))
    comprimento = float(dados.get('comprimento', 0))
    carga_distribuida = float(dados.get('carga_distribuida', 0))
    material_codigo = dados.get('material')
    tipo_apoio = dados.get('tipo_apoio')

    # Validar entradas
    if largura <= 0 or altura <= 0 or comprimento <= 0 or carga_distribuida <= 0:
        return {'erro': 'Todos os valores numéricos devem ser maiores que zero.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}
    if not tipo_apoio:
        return {'erro': 'Tipo de apoio não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Flecha e realizar o cálculo
    flecha = Flecha(
        largura=largura,
        altura=altura,
        comprimento=comprimento,
        carga_distribuida=carga_distribuida,
        material=material_data,
        tipo_apoio=tipo_apoio
    )
    resultado = flecha.gerar_relatorio()

    return resultado

def calcular_detalhamento(dados):
    elemento = dados.get('elemento')
    material_codigo = dados.get('material')
    # Outros parâmetros conforme o elemento

    # Validar entradas
    if not elemento:
        return {'erro': 'Elemento não especificado.'}
    if not material_codigo:
        return {'erro': 'Material não especificado.'}

    # Obter material selecionado
    material_data = next((m for m in MATERIAIS_DISPONIVEIS if m['codigo'] == material_codigo), None)
    if not material_data:
        return {'erro': 'Material selecionado inválido.'}

    # Criar objeto Detalhamento e realizar o cálculo
    detalhamento = Detalhamento(elemento=elemento, material=material_data, **dados)
    resultado = detalhamento.gerar_relatorio()

    return resultado

def calcular_fundacao(dados):
    tipo_fundacao = dados.get('tipo_fundacao')
    carga = float(dados.get('carga', 0))
    profundidade = float(dados.get('profundidade', 0))
    solo_codigo = dados.get('solo')

    # Validar entradas
    if carga <= 0 or profundidade <= 0:
        return {'erro': 'Carga e profundidade devem ser maiores que zero.'}
    if not tipo_fundacao:
        return {'erro': 'Tipo de fundação não especificado.'}
    if not solo_codigo:
        return {'erro': 'Tipo de solo não especificado.'}

    # Obter dados do solo
    solo_data = next((s for s in SOLOS_DISPONIVEIS if s['codigo'] == solo_codigo), None)
    if not solo_data:
        return {'erro': 'Solo selecionado inválido.'}

    # Criar camada de solo usando SoloManager
    solo = SoloManager.criar_camada(solo_codigo, profundidade, **solo_data)

    # Criar objeto fundação usando FundacaoManager
    try:
        fundacao = FundacaoManager.criar_fundacao(
            tipo=tipo_fundacao,
            solo_tipo=solo_codigo,
            profundidade=profundidade,
            carga=carga,
            **dados
        )
    except ValueError as e:
        return {'erro': str(e)}

    # Realizar o cálculo da fundação
    resultado = fundacao.gerar_relatorio()

    return resultado

def obter_estrutura_completa():
    # Retornar a estrutura completa dos campos necessários para cada cálculo
    estrutura = {
        'pilar': {
            'numericos': ['largura', 'altura', 'carga'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS
            }
        },
        'viga': {
            'numericos': ['largura', 'altura', 'comprimento', 'carga'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS,
                'tipo_carga': ['pontual', 'distribuida'],
                'tipo_apoio': ['engastado', 'apoio_simples']
            }
        },
        'laje': {
            'numericos': ['largura', 'comprimento', 'carga'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS
            }
        },
        'arco': {
            'numericos': ['largura', 'espessura', 'raio', 'carga'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS
            }
        },
        'trelica': {
            'numericos': ['largura', 'altura', 'carga'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS
            }
        },
        'viga_continua': {
            'numericos': ['largura', 'altura', 'comprimento_total', 'numero_apoios', 'carga_distribuida'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS
            }
        },
        'flecha': {
            'numericos': ['largura', 'altura', 'comprimento', 'carga_distribuida'],
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS,
                'tipo_apoio': ['engastado', 'apoio_simples']
            }
        },
        'detalhamento': {
            'numericos': [],  # Dependendo do elemento
            'opcoes': {
                'material': MATERIAIS_DISPONIVEIS,
                'elemento': ['viga', 'pilar', 'laje']
            }
        },
        'fundacao': {
            'numericos': ['carga', 'profundidade'],
            'opcoes': {
                'solo': SOLOS_DISPONIVEIS,
                'tipo_fundacao': ['sapata', 'estaca', 'bloco', 'radier', 'tubulão', 'sapata_corrida', 'sapata_rigida', 'barrete']
            }
        }
    }
    return estrutura

# Função para gerar o relatório PDF
def gerar_relatorio_pdf(dados):
    """
    Gera um relatório em PDF baseado nos dados fornecidos.
    Utiliza a biblioteca ReportLab para criar o PDF.

    Args:
        dados (dict): Dicionário contendo os dados para o relatório.

    Returns:
        str: O caminho completo do arquivo PDF gerado.
    """
    # Definir o nome do arquivo com base na data e hora atual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"relatorio_{timestamp}.pdf"

    # Definir o caminho completo do arquivo (certifique-se de que a pasta 'media' existe)
    caminho_arquivo = os.path.join('media', nome_arquivo)

    # Criar o documento
    doc = SimpleDocTemplate(
        caminho_arquivo,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Estilos
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CenterTitle', alignment=TA_CENTER, fontSize=16, spaceAfter=20))
    styles.add(ParagraphStyle(name='LeftHeading', alignment=TA_LEFT, fontSize=12, spaceAfter=10, fontName='Helvetica-Bold'))

    # Lista para armazenar os elementos do relatório
    elements = []

    # Título do relatório
    elements.append(Paragraph("Relatório de Cálculo Estrutural", styles['CenterTitle']))

    # Adicionar data e hora
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elements.append(Paragraph(f"Data e Hora: {data_hora}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Adicionar informações gerais
    elements.append(Paragraph("Informações Gerais:", styles['LeftHeading']))

    tipo = dados.get('tipo', 'Não especificado')
    elements.append(Paragraph(f"Tipo de Elemento: {tipo}", styles['Normal']))

    # Adicionar materiais e outros campos no relatório
    if 'material' in dados:
        elements.append(Paragraph(f"Material: {dados.get('material', 'Não especificado')}", styles['Normal']))
    if 'solo' in dados:
        elements.append(Paragraph(f"Solo: {dados.get('solo', 'Não especificado')}", styles['Normal']))
    if 'tipo_carga' in dados:
        elements.append(Paragraph(f"Tipo de Carga: {dados.get('tipo_carga', 'Não especificado')}", styles['Normal']))
    if 'tipo_apoio' in dados:
        elements.append(Paragraph(f"Tipo de Apoio: {dados.get('tipo_apoio', 'Não especificado')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Adicionar dados específicos com base no tipo
    elements.append(Paragraph("Resultados do Cálculo:", styles['LeftHeading']))

    # Tabela de resultados
    data_table = []

    # Iterar sobre os itens do dicionário e adicionar à tabela
    for chave, valor in dados.items():
        if chave in ['tipo', 'material', 'solo', 'tipo_carga', 'tipo_apoio']:
            continue  # Já adicionados anteriormente
        # Formatar os valores numéricos
        if isinstance(valor, float):
            valor_formatado = f"{valor:.2f}"
        else:
            valor_formatado = str(valor)
        data_table.append([chave.replace('_', ' ').capitalize(), valor_formatado])

    # Definir estilo da tabela
    tabela = Table(data_table, colWidths=[7*cm, 7*cm])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(tabela)

    # Adicionar espaço no final
    elements.append(Spacer(1, 12))

    # Rodapé (pode ser personalizado conforme necessário)
    def rodape(canvas, doc):
        canvas.saveState()
        rodape_texto = "Este é um relatório gerado automaticamente pelo sistema."
        canvas.setFont('Helvetica', 9)
        canvas.drawCentredString(A4[0]/2.0, 1.5*cm, rodape_texto)
        canvas.restoreState()

    # Montar o documento
    doc.build(elements, onLaterPages=rodape, onFirstPage=rodape)

    return caminho_arquivo

# Lista de funções disponíveis para importação
__all__ = [
    'calcular_pilar',
    'calcular_viga',
    'calcular_laje',
    'calcular_arco',
    'calcular_trelica',
    'calcular_viga_continua',
    'calcular_flecha',
    'calcular_detalhamento',
    'calcular_fundacao',
    'gerar_relatorio_pdf',
    'obter_materiais_disponiveis',
    'obter_solos_disponiveis',
    'obter_todas_opcoes',
    'obter_estrutura_completa'
]
