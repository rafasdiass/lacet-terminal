import math
from typing import Dict

class Solo:
    """
    Classe representando as propriedades do solo.
    """
    def __init__(self, tensao_admissivel: float, coeficiente_atrito: float = 0.5):
        """
        Inicializa uma instância de Solo.

        :param tensao_admissivel: Tensão admissível do solo (kN/m²)
        :param coeficiente_atrito: Coeficiente de atrito lateral do solo (padrão: 0.5)
        """
        self.tensao_admissivel = tensao_admissivel
        self.coeficiente_atrito = coeficiente_atrito

class Estaca:
    """
    Classe responsável pelos cálculos de uma fundação do tipo Estaca.
    """

    def __init__(self, carga: float, fck: float, diametro: float, comprimento: float, solo: Solo, peso_concreto: float = 25, fyk: float = 500):
        """
        Inicializa uma instância da fundação Estaca.

        :param carga: Carga aplicada na estaca (kN)
        :param fck: Resistência característica do concreto (MPa)
        :param diametro: Diâmetro da estaca (m)
        :param comprimento: Comprimento da estaca (m)
        :param solo: Instância da classe Solo com propriedades do solo
        :param peso_concreto: Peso específico do concreto (kN/m³) - padrão: 25 kN/m³
        :param fyk: Resistência característica do aço (MPa) - padrão: 500 MPa
        """
        self.carga = carga
        self.fck = fck
        self.diametro = diametro
        self.comprimento = comprimento
        self.solo = solo
        self.peso_concreto = peso_concreto
        self.fyk = fyk

    def calcular_area(self) -> float:
        """
        Calcula a área da seção transversal da estaca (m²).

        :return: Área da seção transversal (m²)
        """
        raio = self.diametro / 2
        return math.pi * raio ** 2

    def calcular_volume_concreto(self) -> float:
        """
        Calcula o volume de concreto da estaca (m³).

        :return: Volume de concreto (m³)
        """
        return self.calcular_area() * self.comprimento

    def calcular_peso_concreto(self) -> float:
        """
        Calcula o peso total do concreto da estaca (kN).

        :return: Peso do concreto (kN)
        """
        return self.calcular_volume_concreto() * self.peso_concreto

    def calcular_tensao_no_solo(self) -> float:
        """
        Calcula a tensão no solo com base na carga aplicada e na capacidade de carga do solo.

        :return: Tensão no solo (kN/m²)
        """
        area = self.calcular_area()
        return self.carga / area

    def verificar_segurança_tensao_solo(self) -> bool:
        """
        Verifica se a tensão no solo está dentro dos limites seguros com base na capacidade do solo.

        :return: True se a tensão estiver segura, False se exceder a capacidade do solo.
        """
        tensao_no_solo = self.calcular_tensao_no_solo()
        return tensao_no_solo <= self.solo.tensao_admissivel

    def calcular_carga_admissivel(self) -> float:
        """
        Calcula a carga admissível da estaca de acordo com a capacidade do solo.

        :return: Carga admissível (kN)
        """
        return self.solo.tensao_admissivel * self.calcular_area()

    def verificar_ruptura_solo(self) -> bool:
        """
        Verifica se há risco de ruptura do solo, comparando a carga aplicada com a carga admissível do solo.

        :return: True se houver risco de ruptura, False caso contrário.
        """
        return self.carga > self.calcular_carga_admissivel()

    def calcular_armacao(self) -> Dict[str, float]:
        """
        Calcula a armadura necessária para a estaca.

        :return: Dicionário com a quantidade de barras e diâmetro
        """
        # Proporção mínima de aço para estacas em regiões comprimidas
        armadura_minima = 0.002  # 2% da área da seção transversal
        area_aco = armadura_minima * self.calcular_area()  # Área de aço necessária (m²)

        # Assumindo barras de 20 mm de diâmetro para o cálculo
        diametro_barras = 20 / 1000  # 20 mm em metros
        area_barra = (math.pi * diametro_barras ** 2) / 4  # Área de uma barra (m²)

        quantidade_barras = area_aco / area_barra  # Número de barras necessárias

        return {
            "quantidade_barras": quantidade_barras,
            "diametro_barras": diametro_barras * 1000  # Convertendo para mm
        }

    def calcular_resistencia_cisalhamento(self) -> float:
        """
        Calcula a tensão de cisalhamento na estaca e verifica se está dentro dos limites permitidos para o concreto.

        :return: Tensão de cisalhamento (MPa)
        """
        area_cisalhamento = self.diametro * self.comprimento
        tensao_cisalhamento = self.carga / area_cisalhamento
        resistencia_corte_concreto = 0.6 * math.sqrt(self.fck)

        if tensao_cisalhamento > resistencia_corte_concreto:
            raise ValueError("A estaca falha por cisalhamento.")

        return tensao_cisalhamento

    def verificar_estabilidade_arrancamento(self) -> bool:
        """
        Verifica a estabilidade da estaca ao arrancamento considerando o peso da estaca e a resistência de atrito lateral.

        :return: True se a estaca for estável ao arrancamento, False caso contrário.
        """
        peso_proprio_estaca = self.calcular_volume_concreto() * self.peso_concreto
        resistencia_atrito_lateral = math.pi * self.diametro * self.comprimento * self.solo.tensao_admissivel * self.solo.coeficiente_atrito
        resistencia_total_arrancamento = peso_proprio_estaca + resistencia_atrito_lateral

        return resistencia_total_arrancamento >= self.carga

    def gerar_relatorio(self) -> Dict[str, float]:
        """
        Gera um relatório completo com todos os cálculos da estaca.

        :return: Dicionário contendo os resultados dos cálculos
        """
        return {
            "Área da Seção Transversal (m²)": self.calcular_area(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_no_solo(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Peso do Concreto (kN)": self.calcular_peso_concreto(),
            "Carga Admissível (kN)": self.calcular_carga_admissivel(),
            "Ruptura do Solo": self.verificar_ruptura_solo(),
            "Armadura - Quantidade de Barras": self.calcular_armacao()["quantidade_barras"],
            "Armadura - Diâmetro das Barras (mm)": self.calcular_armacao()["diametro_barras"],
            "Tensão de Cisalhamento (MPa)": self.calcular_resistencia_cisalhamento(),
            "Estabilidade ao Arrancamento": self.verificar_estabilidade_arrancamento()
        }
