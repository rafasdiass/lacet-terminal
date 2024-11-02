import math
from typing import Dict

class Bloco:
    """
    Classe responsável pelos cálculos de uma fundação do tipo Bloco.
    """

    def __init__(self, carga: float, fck: float, largura: float, comprimento: float, altura: float, peso_concreto: float = 25, solo=None):
        """
        Inicializa uma instância da fundação Bloco.

        :param carga: Carga aplicada no bloco (kN)
        :param fck: Resistência característica do concreto (MPa)
        :param largura: Largura do bloco (m)
        :param comprimento: Comprimento do bloco (m)
        :param altura: Altura do bloco (m)
        :param peso_concreto: Peso específico do concreto (kN/m³) - padrão: 25 kN/m³
        :param solo: Objeto representando as propriedades do solo
        """
        self.carga = carga
        self.fck = fck
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        self.peso_concreto = peso_concreto
        self.solo = solo  # Objeto de solo que armazena propriedades como tipo e capacidade de carga

        # Atualiza a capacidade do solo a partir do objeto de solo, se ele for fornecido
        if self.solo and hasattr(self.solo, 'capacidade_carga'):
            self.capacidade_solo = self.solo.capacidade_carga
        else:
            # Valor padrão caso o solo não seja fornecido
            self.capacidade_solo = 0.4 * self.fck

    def calcular_area(self) -> float:
        """
        Calcula a área da base do bloco (m²).
        """
        return self.largura * self.comprimento

    def calcular_volume_concreto(self) -> float:
        """
        Calcula o volume de concreto do bloco (m³).
        """
        return self.calcular_area() * self.altura

    def calcular_peso_concreto(self) -> float:
        """
        Calcula o peso total do concreto do bloco (kN).
        """
        return self.calcular_volume_concreto() * self.peso_concreto

    def calcular_tensao_solo(self) -> float:
        """
        Calcula a tensão no solo com base na carga aplicada e na área da base do bloco.
        """
        return self.carga / self.calcular_area()

    def verificar_segurança_tensao(self) -> bool:
        """
        Verifica se a tensão no solo está dentro dos limites aceitáveis para a resistência do solo.
        """
        tensao_solo = self.calcular_tensao_solo()
        return tensao_solo <= self.capacidade_solo

    def calcular_armacao_flexao(self) -> Dict[str, float]:
        """
        Calcula a armadura necessária para resistir ao momento fletor.
        """
        momento_fletor = (self.carga * self.comprimento) / 8  # Momento fletor máximo
        d = self.altura - 0.05  # Altura útil com coberto nominal de 5 cm
        momento_admissivel = 0.251 * self.fck * (d ** 2)  # Momento admissível

        if momento_fletor > momento_admissivel:
            raise ValueError("O bloco é insuficiente para resistir ao momento fletor calculado.")

        area_aco_necessaria = momento_fletor / (0.87 * 500 * d)  # Tensão do aço assumida como 500 MPa

        # Supondo barras de aço de 16 mm
        diametro_barras = 16 / 1000  # 16 mm em metros
        area_barra = (math.pi * diametro_barras ** 2) / 4  # Área de uma barra (m²)
        quantidade_barras = area_aco_necessaria / area_barra  # Número de barras necessárias

        return {
            "quantidade_barras": quantidade_barras,
            "diametro_barras": diametro_barras * 1000  # Converter para mm
        }

    def calcular_resistencia_cisalhamento(self) -> float:
        """
        Calcula a tensão de cisalhamento no bloco e verifica a resistência ao cisalhamento.
        """
        area_cisalhamento = self.largura * self.altura
        tensao_cisalhamento = self.carga / area_cisalhamento
        resistencia_corte_concreto = 0.6 * math.sqrt(self.fck)

        if tensao_cisalhamento > resistencia_corte_concreto:
            raise ValueError("O bloco falha por cisalhamento.")

        return tensao_cisalhamento

    def calcular_armacao_cisalhamento(self) -> Dict[str, float]:
        """
        Calcula a armadura necessária para resistir ao cisalhamento.
        """
        armadura_minima_cisalhamento = 0.0015
        area_aco_cisalhamento = armadura_minima_cisalhamento * self.largura * self.altura  # Área de aço (m²)

        # Supondo barras de aço de 8 mm para estribos
        diametro_estribo = 8 / 1000  # 8 mm em metros
        area_estribo = (math.pi * diametro_estribo ** 2) / 4  # Área de um estribo (m²)
        quantidade_estribos = area_aco_cisalhamento / area_estribo  # Número de estribos necessários

        return {
            "quantidade_estribos": quantidade_estribos,
            "diametro_estribo": diametro_estribo * 1000  # Converter para mm
        }

    def gerar_relatorio(self) -> Dict[str, float]:
        """
        Gera um relatório detalhado com todos os cálculos do bloco.
        """
        return {
            "Área do Bloco (m²)": self.calcular_area(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_solo(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Peso do Concreto (kN)": self.calcular_peso_concreto(),
            "Segurança na Tensão do Solo": self.verificar_segurança_tensao(),
            "Armadura de Flexão - Quantidade de Barras": self.calcular_armacao_flexao()["quantidade_barras"],
            "Armadura de Flexão - Diâmetro das Barras (mm)": self.calcular_armacao_flexao()["diametro_barras"],
            "Tensão de Cisalhamento (MPa)": self.calcular_resistencia_cisalhamento(),
            "Armadura de Cisalhamento - Quantidade de Estribos": self.calcular_armacao_cisalhamento()["quantidade_estribos"],
            "Armadura de Cisalhamento - Diâmetro dos Estribos (mm)": self.calcular_armacao_cisalhamento()["diametro_estribo"]
        }
