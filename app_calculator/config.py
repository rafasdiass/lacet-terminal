# Configurações gerais de materiais e propriedades mecânicas

# Resistência característica do concreto (MPa)
FCK_CONCRETO_PADRAO = 25.0  # Utilizado para elementos de concreto, como sapatas, pilares, etc.

# Resistência característica do aço (MPa)
FYK_ACO_PADRAO = 500.0      # Utilizado para elementos de aço, se necessário

# Peso específico do concreto (kN/m³)
PESO_ESPECIFICO_CONCRETO = 25.0

# Módulo de elasticidade do aço (Pa)
MODULO_ELASTICIDADE_ACO = 210e9  # 210 GPa, típico para aço

# Tensão admissível do solo (kN/m²) - usada como limite de tensão para fundações
TENSAO_ADMISSIVEL_SOLO_PADRAO = 150.0

# Proporções mínimas de aço para elementos estruturais (como fração da seção)
ARMADURA_MINIMA_PILAR = 0.0020      # 0,20% da seção para pilares
ARMADURA_MINIMA_VIGA = 0.0015       # 0,15% da seção para vigas
ARMADURA_MINIMA_LAJE = 0.0010       # 0,10% da seção para lajes
ARMADURA_MINIMA_TUBULAO = 0.0025    # 0,25% da seção para tubulões
ARMADURA_MINIMA_RADIER = 0.0015     # 0,15% da seção para radier

# Raio padrão para cálculos de arco (metros)
RAIO_CIRCULAR_PADRAO = 0.05  # Exemplo de raio em metros, pode ser usado para cálculo de arco, etc.

# Área de seção transversal padrão (m²) - exemplo para cálculo de análise estrutural
AREA_SECAO_PADRAO = 0.01  # Usado no exemplo para barras de análise estrutural

# Coeficiente de segurança adicional para análises (exemplo para ensaios adicionais de segurança, caso necessário)
COEFICIENTE_SEGURANCA_PADRAO = 1.5

# Módulo de deformação típico para solos (Pa) - para cálculo de assentamentos
MODULO_DEFORMACAO_SOLO = 15000  # Valor típico em kN/m², ajuste conforme o tipo de solo

# Valores padrão para tipos de peças, para facilitar a inicialização em testes e simulações
TIPOS_PECA_VALIDOS = [
    "pilar", "viga", "laje", "fundacao", "arco", "trelica", 
    "viga_continua", "flecha", "detalhamento"
]

# Mensagens padrão para uso na interface de usuário
MENSAGEM_OPCAO_INVALIDA = "Opção inválida. Escolha novamente."
MENSAGEM_VALORES_POSITIVOS = "A largura, altura e carga devem ser valores positivos."

# Configurações de relatório e saída
CAMINHO_PADRAO_MEMORIA_CALCULO = "memoria_calculo.txt"
CAMINHO_PADRAO_RELATORIO_PDF = "relatorio_calculo.pdf"

# Definições de unidades
UNIDADE_CARGA = "kN"
UNIDADE_COMPRIMENTO = "m"
UNIDADE_AREA = "m²"
UNIDADE_PRESSAO = "kN/m²"
UNIDADE_MOMENTO = "kN.m"

# Formatação de valores para saída
FORMATO_AREA = "{:.2f} m²"
FORMATO_PRESSAO = "{:.2f} kN/m²"
FORMATO_MOMENTO = "{:.2f} kN.m"
FORMATO_TENSAO = "{:.2f} MPa"
FORMATO_CARGA = "{:.2f} kN"
FORMATO_COMPRIMENTO = "{:.2f} m"
FORMATO_DESLOCAMENTO = "{:.4f} m"  # Para resultados de deslocamento estrutural
FORMATO_REACAO = "{:.2f} kN"

# Configurações de geração de relatórios PDF
TITULO_RELATORIO_PDF = "Relatório de Cálculo Estrutural - LCT Calculator"
TEXTO_ASSINATURA_ENGENHEIRO = "Assinatura do engenheiro responsável"
DATA_GERACAO_RELATORIO = "Data de geração do relatório: "

# Variáveis para uso em cálculos específicos
PROPORCAO_ARMADURA_PILAR = 0.002  # Proporção mínima de aço para pilares
PROPORCAO_ARMADURA_LAJE = 0.001   # Proporção mínima de aço para lajes
PROPORCAO_ARMADURA_TUBULAO = 0.0025  # Proporção mínima de aço para tubulões

# Módulos e valores auxiliares
MODULO_ELASTICIDADE_CONCRETO = 30e9  # Pa, valor médio para concreto
