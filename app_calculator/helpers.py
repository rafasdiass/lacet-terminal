# helpers.py

import math
# Importar classes de fundação e estruturas

# Atualize os imports para apontar diretamente para os módulos onde as classes estão definidas
from .estruturas.pilar import Pilar
from .estruturas.viga import Viga
from .estruturas.laje import Laje
from .estruturas.arco import Arco
from .estruturas.trelica import Trelica
from .estruturas.viga_continua import VigaContinua
from .estruturas.flecha import Flecha
from .estruturas.detalhamento import Detalhamento

from .fundacoes.sapata import Sapata
from .fundacoes.sapata_rigida import SapataRigida
from .fundacoes.sapata_corrida import SapataCorrida
from .fundacoes.bloco import Bloco
from .fundacoes.tubulao import Tubulao
from .fundacoes.tubulao_ceu_aberto import TubulaoCeuAberto
from .fundacoes.tubulao_ar_comprimido import TubulaoArComprimido
from .fundacoes.estaca import Estaca
from .fundacoes.estaca_helice_continua import EstacaHeliceContinua
from .fundacoes.radier import Radier
from .fundacoes.barrete import Barrete

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
    tensao = carga / area if area > 0 else 0
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
    tensao = carga / area if area > 0 else 0
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
    momento = (carga * comprimento**2) / 8  # Fórmula para momento em viga contínua
    inercia = (largura * altura**3) / 12
    tensao = (momento * (altura / 2)) / inercia
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
    
    E = 210000  # Módulo de elasticidade do aço em MPa
    I = (largura * altura**3) / 12  # Momento de inércia
    deflexao = (5 * carga * comprimento**4) / (384 * E * I)
    verificacao = "Deflexão dentro dos limites aceitáveis." if deflexao < 0.03 * comprimento else "Deflexão excessiva."
    return {
        'tipo': 'Flecha',
        'largura': largura,
        'altura': altura,
        'comprimento': comprimento,
        'carga': carga,
        'deflexao': deflexao,
        'verificacao': verificacao
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

    resultado = fundacao.gerar_relatorio()  # Assumindo que cada classe tem um método gerar_relatorio()
    return resultado

def obter_estrutura_completa():
    # Implementar a função para retornar a estrutura completa dos campos
    # Pode ser um dicionário com informações sobre os campos necessários para cada cálculo
    estrutura = {
        'pilar': ['largura', 'altura', 'carga'],
        'viga': ['largura', 'altura', 'carga', 'comprimento'],
        # Adicionar para os demais tipos
    }
    return estrutura

def gerar_relatorio_pdf(dados):
    """
    Gera um relatório em PDF baseado nos dados fornecidos.
    Utiliza a biblioteca ReportLab para criar o PDF.

    Args:
        dados (dict): Dicionário contendo os dados para o relatório.

    Returns:
        str: O nome do arquivo PDF gerado.
    """
    # Definir o nome do arquivo com base na data e hora atual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"relatorio_{timestamp}.pdf"

    # Definir o caminho completo do arquivo
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

    # Adicionar dados específicos com base no tipo
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Resultados do Cálculo:", styles['LeftHeading']))

    # Tabela de resultados
    data_table = []

    # Iterar sobre os itens do dicionário e adicionar à tabela
    for chave, valor in dados.items():
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