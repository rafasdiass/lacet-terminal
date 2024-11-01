# Código para a classe Laje
from typing import Dict

class Laje:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area = self.largura * self.altura
        return {
            "Área da Laje (m²)": area,
            "Carga Aplicada (kN)": self.carga
        }
