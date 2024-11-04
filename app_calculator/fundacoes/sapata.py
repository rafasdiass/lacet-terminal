from typing import Dict
import math

class Solo:
    def __init__(self, tipo: str, capacidade_carga: float, peso_especifico: float, angulo_atrito: float):
        self.tipo = tipo
        self.capacidade_carga = capacidade_carga  # Capacidade de carga do solo (kN/m²)
        self.peso_especifico = peso_especifico  # Peso específico do solo (kN/m³)
        self.angulo_atrito = angulo_atrito  # Ângulo de atrito interno do solo (em graus)

class Sapata:
    def __init__(self, carga: float, fck: float, base: float, altura: float, solo: Solo, peso_concreto: float = 25, coef_puncionamento: float = 0.8):
        self.carga = carga
        self.fck = fck
        self.base = base
        self.altura = altura
        self.solo = solo
        self.peso_concreto = peso_concreto
        self.coef_puncionamento = coef_puncionamento

    def calcular_area(self) -> float:
        return self.base ** 2

    def calcular_volume_concreto(self) -> float:
        return self.calcular_area() * self.altura

    def calcular_peso_concreto(self) -> float:
        return self.calcular_volume_concreto() * self.peso_concreto

    def calcular_tensao_no_solo(self) -> float:
        return self.carga / self.calcular_area()

    def calcular_carga_admissivel(self) -> float:
        return self.solo.capacidade_carga * self.calcular_area()

    def verificar_ruptura_solo(self) -> bool:
        return self.carga > self.calcular_carga_admissivel()

    def calcular_momento_fletor(self) -> float:
        return self.carga * self.base / 2

    def calcular_armacao_flexao(self) -> Dict[str, float]:
        momento_fletor = self.calcular_momento_fletor()
        d = self.altura - 0.05
        area_aco = momento_fletor / (0.87 * 500 * d)
        diametro_barras = 16 / 1000
        area_barra = (math.pi * diametro_barras ** 2) / 4
        quantidade_barras = math.ceil(area_aco / area_barra)
        return {"quantidade_barras": quantidade_barras, "diametro_barras": diametro_barras * 1000}

    def calcular_tensao_cisalhamento(self) -> float:
        area_cisalhamento = self.base * self.altura
        tensao_cisalhamento = self.carga / area_cisalhamento
        resistencia_corte_concreto = 0.6 * math.sqrt(self.fck)
        if tensao_cisalhamento > resistencia_corte_concreto:
            raise ValueError("A sapata falha por cisalhamento.")
        return tensao_cisalhamento

    def calcular_puncionamento(self) -> float:
        perimetro_critico = 4 * self.coef_puncionamento * self.base
        area_critica = perimetro_critico * self.altura
        return self.carga / area_critica

    def verificar_estabilidade_deslizamento(self) -> bool:
        forca_normal = self.calcular_peso_concreto()
        resistencia_deslizamento = forca_normal * math.tan(math.radians(self.solo.angulo_atrito))
        if resistencia_deslizamento < self.carga:
            raise ValueError("A sapata não é estável ao deslizamento.")
        return True

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Área da Base (m²)": self.calcular_area(),
            "Tensão no Solo (kN/m²)": self.calcular_tensao_no_solo(),
            "Volume de Concreto (m³)": self.calcular_volume_concreto(),
            "Peso do Concreto (kN)": self.calcular_peso_concreto(),
            "Carga Admissível (kN)": self.calcular_carga_admissivel(),
            "Ruptura do Solo": self.verificar_ruptura_solo(),
            "Momento Fletor (kN.m)": self.calcular_momento_fletor(),
            "Armadura - Quantidade de Barras": self.calcular_armacao_flexao()["quantidade_barras"],
            "Armadura - Diâmetro das Barras (mm)": self.calcular_armacao_flexao()["diametro_barras"],
            "Tensão de Cisalhamento (MPa)": self.calcular_tensao_cisalhamento(),
            "Tensão de Puncionamento (kN/m²)": self.calcular_puncionamento(),
            "Estabilidade ao Deslizamento": self.verificar_estabilidade_deslizamento()
        }
