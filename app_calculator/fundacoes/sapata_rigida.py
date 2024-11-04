from typing import Dict
import math

class Solo:
    def __init__(self, tipo: str, capacidade_carga: float, peso_especifico: float, angulo_atrito: float):
        self.tipo = tipo
        self.capacidade_carga = capacidade_carga  # kN/m²
        self.peso_especifico = peso_especifico  # kN/m³
        self.angulo_atrito = math.radians(angulo_atrito)  # Converte de graus para radianos

class SapataRigida:
    def __init__(self, carga: float, largura: float, altura: float, fck: float, solo: Solo):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.fck = fck
        self.solo = solo

    def calcular_area_base(self) -> float:
        return self.largura ** 2

    def calcular_volume_concreto(self) -> float:
        return self.calcular_area_base() * self.altura

    def calcular_tensao_solo(self) -> float:
        return self.carga / self.calcular_area_base()

    def verificar_ruptura_solo(self) -> bool:
        return self.calcular_tensao_solo() > self.solo.capacidade_carga

    def calcular_armacao(self) -> Dict[str, float]:
        momento_fletor = self.carga * self.largura / 2
        d = self.altura - 0.05  # Altura útil considerando o cobrimento
        area_aco = momento_fletor / (0.87 * 500 * d)

        diametro_barras = 16 / 1000  # 16 mm em metros
        area_barra = (math.pi * diametro_barras ** 2) / 4
        quantidade_barras = math.ceil(area_aco / area_barra)

        return {
            "quantidade_barras": quantidade_barras,
            "diametro_barras": diametro_barras * 1000  # Converter para mm
        }

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Área Base da Sapata Rígida (m²)": self.calcular_area_base(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_solo(),
            "Capacidade de Carga do Solo (kN/m²)": self.solo.capacidade_carga,
            "Ruptura do Solo": self.verificar_ruptura_solo(),
            "Armadura - Quantidade de Barras": self.calcular_armacao()["quantidade_barras"],
            "Armadura - Diâmetro das Barras (mm)": self.calcular_armacao()["diametro_barras"]
        }
