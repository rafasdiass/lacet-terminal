from typing import Dict, Tuple
import math

class Solo:
    """Classe que representa as propriedades do solo."""
    def __init__(self, capacidade_carga: float, angulo_atrito: float, peso_proprio: float):
        self.capacidade_carga = capacidade_carga  # Capacidade de carga do solo (kN/m²)
        self.angulo_atrito = math.radians(angulo_atrito)  # Converte o ângulo de atrito de graus para radianos
        self.peso_proprio = peso_proprio  # Peso próprio do solo (kN/m³)

class SapataCorrida:
    """Classe responsável pelo cálculo de uma Sapata Corrida."""

    def __init__(self, largura_base: float, altura_sapata: float, comprimento_sapata: float, fck: float, carga_kN: float,
                 cobrimento: float, diametro_aco: float, solo: Solo):
        self.largura_base = largura_base
        self.altura_sapata = altura_sapata
        self.comprimento_sapata = comprimento_sapata
        self.fck = fck
        self.carga_kN = carga_kN
        self.cobrimento = cobrimento / 1000  # Converte de mm para metros
        self.diametro_aco = diametro_aco / 1000  # Converte de mm para metros
        self.solo = solo  # Instância da classe Solo

    def calcular_tensao_solo(self) -> float:
        """Calcula a tensão admissível no solo devido à carga."""
        area_base = self.largura_base * self.comprimento_sapata
        tensao_solo = self.carga_kN / area_base
        return tensao_solo

    def calcular_armadura_flexao(self) -> Tuple[float, int]:
        momento_fletor_max = (self.carga_kN * self.largura_base) / 8
        d = self.altura_sapata - self.cobrimento
        area_aco_necessaria = momento_fletor_max / (0.87 * 500 * d)

        diametro_barras = 20 / 1000
        area_barra = (math.pi * diametro_barras ** 2) / 4
        numero_barras = math.ceil(area_aco_necessaria / area_barra)

        return area_aco_necessaria * 10000, numero_barras

    def calcular_cisalhamento(self) -> float:
        area_cisalhamento = self.largura_base * self.altura_sapata
        tensao_cisalhamento = self.carga_kN / area_cisalhamento
        resistencia_corte_concreto = 0.6 * math.sqrt(self.fck)

        if tensao_cisalhamento > resistencia_corte_concreto:
            raise ValueError("A sapata falha por cisalhamento.")

        return tensao_cisalhamento

    def verificar_estabilidade(self) -> bool:
        forca_normal_solo = self.carga_kN - (self.solo.peso_proprio * self.largura_base * self.altura_sapata)
        resistencia_deslizamento = forca_normal_solo * math.tan(self.solo.angulo_atrito)

        if resistencia_deslizamento < self.carga_kN:
            raise ValueError("A sapata não é estável ao deslizamento.")
        
        return True

    def calcular_volume_concreto(self) -> float:
        return self.largura_base * self.comprimento_sapata * self.altura_sapata

    def calcular(self) -> Dict[str, float]:
        resultados = {
            "Tensão no solo (kN/m²)": self.calcular_tensao_solo(),
            "Área de aço necessária (cm²)": self.calcular_armadura_flexao()[0],
            "Número de barras de aço": self.calcular_armadura_flexao()[1],
            "Tensão de cisalhamento (MPa)": self.calcular_cisalhamento(),
            "Volume de concreto (m³)": self.calcular_volume_concreto(),
            "Estabilidade ao deslizamento": self.verificar_estabilidade(),
        }
        return resultados
