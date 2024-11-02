from typing import Dict
import math

class Solo:
    def __init__(self, tipo: str, capacidade_carga: float, coeficiente_atrito: float, compressibilidade: float):
        """
        Inicializa uma instância de solo com suas propriedades.
        
        :param tipo: Tipo do solo (argiloso, arenoso, rochoso, etc.)
        :param capacidade_carga: Capacidade de carga do solo (kN/m²)
        :param coeficiente_atrito: Coeficiente de atrito do solo
        :param compressibilidade: Módulo de deformação do solo (kN/m²)
        """
        self.tipo = tipo
        self.capacidade_carga = capacidade_carga
        self.coeficiente_atrito = coeficiente_atrito
        self.compressibilidade = compressibilidade

class Tubulao:
    """
    Classe responsável pelos cálculos de uma fundação do tipo Tubulão.
    """

    def __init__(self, carga: float, fck: float, diametro: float, altura: float, tipo: str, escavacao_prof: float, 
                 profundidade_agua: float, solo: Solo):
        """
        Inicializa uma instância da fundação Tubulão.

        :param carga: Carga aplicada no tubulão (kN)
        :param fck: Resistência característica do concreto (MPa)
        :param diametro: Diâmetro do tubulão (m)
        :param altura: Altura do tubulão (m)
        :param tipo: Tipo de tubulão ("Céu Aberto" ou "Sob Ar Comprimido")
        :param escavacao_prof: Profundidade da escavação (m)
        :param profundidade_agua: Profundidade do nível freático (m)
        :param solo: Objeto da classe Solo contendo as propriedades do solo
        """
        self.carga = carga
        self.fck = fck
        self.diametro = diametro
        self.altura = altura
        self.tipo = tipo
        self.escavacao_prof = escavacao_prof
        self.profundidade_agua = profundidade_agua
        self.solo = solo

    def calcular_area(self) -> float:
        """
        Calcula a área da base do tubulão (m²).

        :return: Área da base (m²)
        """
        raio = self.diametro / 2
        return math.pi * raio ** 2

    def calcular_volume_concreto(self) -> float:
        """
        Calcula o volume de concreto do tubulão (m³).

        :return: Volume de concreto (m³)
        """
        return self.calcular_area() * self.altura

    def calcular_tensao_no_solo(self) -> float:
        """
        Calcula a tensão no solo (kN/m²) de acordo com a carga aplicada e a área do tubulão.

        :return: Tensão no solo (kN/m²)
        """
        area = self.calcular_area()
        return self.carga / area

    def calcular_carga_admissivel(self) -> float:
        """
        Calcula a carga admissível com base na capacidade do solo.

        :return: Carga admissível (kN)
        """
        return self.solo.capacidade_carga * self.calcular_area()

    def verificar_ruptura_solo(self) -> bool:
        """
        Verifica se há risco de ruptura do solo.

        :return: True se houver risco de ruptura, False caso contrário.
        """
        return self.carga > self.calcular_carga_admissivel()

    def calcular_pressao_lateral(self) -> float:
        """
        Calcula a pressão lateral de água no tubulão (kN/m²) com base na profundidade da água.

        :return: Pressão lateral de água (kN/m²)
        """
        densidade_agua = 1000  # kg/m³
        gravidade = 9.81  # m/s²
        return self.profundidade_agua * densidade_agua * gravidade / 1000  # Convertendo para kN/m²

    def verificar_estabilidade_deslizamento(self) -> bool:
        """
        Verifica a estabilidade ao deslizamento com base no coeficiente de atrito do solo.

        :return: True se for estável ao deslizamento, False caso contrário.
        """
        forca_normal = self.carga  # Considerando que a carga é a força normal
        resistencia_deslizamento = forca_normal * self.solo.coeficiente_atrito
        return resistencia_deslizamento >= self.carga

    def calcular_assentamento(self) -> float:
        """
        Calcula o assentamento esperado do solo com base na compressibilidade do solo.

        :return: Assentamento do solo (mm)
        """
        tensao_no_solo = self.calcular_tensao_no_solo()
        assentamento = (tensao_no_solo / self.solo.compressibilidade) * self.altura * 1000  # Convertendo para mm
        return assentamento

    def gerar_relatorio(self) -> Dict[str, float]:
        """
        Gera um relatório completo com todos os cálculos do tubulão.

        :return: Dicionário contendo os resultados dos cálculos
        """
        return {
            "Área da Base (m²)": self.calcular_area(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_no_solo(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Pressão Lateral da Água (kN/m²)": self.calcular_pressao_lateral(),
            "Carga Admissível (kN)": self.calcular_carga_admissivel(),
            "Ruptura do Solo": self.verificar_ruptura_solo(),
            "Estabilidade ao Deslizamento": self.verificar_estabilidade_deslizamento(),
            "Assentamento Estimado do Solo (mm)": self.calcular_assentamento()
        }
