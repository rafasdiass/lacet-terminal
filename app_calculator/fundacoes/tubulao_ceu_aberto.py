from typing import Dict
import math

class Solo:
    """
    Classe para representar as propriedades do solo.
    """
    def __init__(self, tipo: str, capacidade_carga: float, coeficiente_atrito: float, compressibilidade: float):
        """
        Inicializa uma instância de Solo.
        :param tipo: Tipo de solo (ex: "argiloso", "arenoso")
        :param capacidade_carga: Capacidade de carga do solo (kN/m²)
        :param coeficiente_atrito: Coeficiente de atrito do solo
        :param compressibilidade: Módulo de deformação do solo (kN/m²)
        """
        self.tipo = tipo
        self.capacidade_carga = capacidade_carga
        self.coeficiente_atrito = coeficiente_atrito
        self.compressibilidade = compressibilidade

class TubulaoCeuAberto:
    """
    Classe responsável pelos cálculos de uma fundação do tipo Tubulão Céu Aberto.
    """

    def __init__(self, carga: float, fck: float, diametro: float, profundidade: float, solo: Solo, peso_concreto: float = 25):
        """
        Inicializa uma instância da fundação Tubulão Céu Aberto.

        :param carga: Carga total aplicada sobre o tubulão (kN)
        :param fck: Resistência característica do concreto (MPa)
        :param diametro: Diâmetro do tubulão (m)
        :param profundidade: Profundidade do tubulão (m)
        :param solo: Instância da classe Solo com as propriedades do solo
        :param peso_concreto: Peso específico do concreto (kN/m³) - padrão: 25 kN/m³
        """
        self.carga = carga
        self.fck = fck
        self.diametro = diametro
        self.profundidade = profundidade
        self.solo = solo
        self.peso_concreto = peso_concreto

    def calcular_area_base(self) -> float:
        """Calcula a área da base do tubulão (m²)."""
        return math.pi * (self.diametro / 2) ** 2

    def calcular_volume_concreto(self) -> float:
        """Calcula o volume de concreto necessário para o tubulão (m³)."""
        return self.calcular_area_base() * self.profundidade

    def calcular_peso_concreto(self) -> float:
        """Calcula o peso total do concreto do tubulão (kN)."""
        return self.calcular_volume_concreto() * self.peso_concreto

    def calcular_tensao_no_solo(self) -> float:
        """Calcula a tensão no solo com base na carga aplicada sobre o tubulão."""
        return self.carga / self.calcular_area_base()

    def calcular_carga_admissivel(self) -> float:
        """Calcula a carga admissível do tubulão com base na capacidade do solo."""
        return self.solo.capacidade_carga * self.calcular_area_base()

    def verificar_ruptura_solo(self) -> bool:
        """Verifica se há risco de ruptura do solo."""
        return self.carga > self.calcular_carga_admissivel()

    def calcular_armacao_longitudinal(self) -> Dict[str, float]:
        """Calcula a armadura longitudinal necessária para o tubulão."""
        armadura_minima = 0.0025  # Proporção mínima de aço para tubulão
        area_aco = armadura_minima * self.calcular_area_base()

        # Supondo barras de 20 mm de diâmetro
        diametro_barras = 20 / 1000
        area_barra = (math.pi * diametro_barras ** 2) / 4

        quantidade_barras = area_aco / area_barra

        return {
            "quantidade_barras": quantidade_barras,
            "diametro_barras": diametro_barras * 1000  # mm
        }

    def calcular_armacao_transversal(self) -> Dict[str, float]:
        """Calcula a armadura transversal (estribos) necessária para o tubulão."""
        armadura_minima = 0.0015
        area_aco_transversal = armadura_minima * self.diametro * self.profundidade

        # Supondo barras de 12 mm para estribos
        diametro_estribos = 12 / 1000
        area_estribo = (math.pi * diametro_estribos ** 2) / 4

        quantidade_estribos = area_aco_transversal / area_estribo

        return {
            "quantidade_estribos": quantidade_estribos,
            "diametro_estribos": diametro_estribos * 1000  # mm
        }

    def calcular_assentamento_solo(self) -> float:
        """Calcula o assentamento esperado do solo com base na tensão aplicada."""
        tensao_no_solo = self.calcular_tensao_no_solo()
        assentamento = (tensao_no_solo / self.solo.compressibilidade) * self.profundidade * 1000  # Conversão para mm
        return assentamento

    def verificar_estabilidade_deslizamento(self) -> bool:
        """Verifica a estabilidade ao deslizamento."""
        resistencia_lateral = self.solo.coeficiente_atrito * self.calcular_area_base() * self.solo.capacidade_carga
        return self.carga <= resistencia_lateral

    def verificar_estabilidade_tombamento(self) -> bool:
        """Verifica a estabilidade ao tombamento do tubulão."""
        momento_resistente = self.peso_concreto * (self.diametro / 2)
        momento_aplicado = self.carga * (self.profundidade / 2)
        return momento_resistente >= momento_aplicado

    def verificar_resistencia_cisalhamento(self) -> bool:
        """Verifica se o concreto resiste à tensão de cisalhamento."""
        area_cisalhamento = self.calcular_area_base()
        tensao_cisalhamento = self.carga / area_cisalhamento
        resistencia_corte_concreto = 0.6 * math.sqrt(self.fck) * 1000  # Conversão de MPa para kN/m²
        return tensao_cisalhamento <= resistencia_corte_concreto

    def gerar_relatorio(self) -> Dict[str, float]:
        """Gera um relatório completo com os cálculos do tubulão."""
        return {
            "Área da Base (m²)": self.calcular_area_base(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Peso do Concreto (kN)": self.calcular_peso_concreto(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_no_solo(),
            "Carga Admissível (kN)": self.calcular_carga_admissivel(),
            "Ruptura do Solo": self.verificar_ruptura_solo(),
            "Armadura Longitudinal - Quantidade de Barras": self.calcular_armacao_longitudinal()["quantidade_barras"],
            "Armadura Longitudinal - Diâmetro das Barras (mm)": self.calcular_armacao_longitudinal()["diametro_barras"],
            "Armadura Transversal - Quantidade de Estribos": self.calcular_armacao_transversal()["quantidade_estribos"],
            "Armadura Transversal - Diâmetro dos Estribos (mm)": self.calcular_armacao_transversal()["diametro_estribos"],
            "Assentamento Estimado do Solo (mm)": self.calcular_assentamento_solo(),
            "Estabilidade ao Deslizamento": self.verificar_estabilidade_deslizamento(),
            "Estabilidade ao Tombamento": self.verificar_estabilidade_tombamento(),
            "Resistência ao Cisalhamento do Concreto": self.verificar_resistencia_cisalhamento()
        }
