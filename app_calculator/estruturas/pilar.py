# Código para a classe Pilar
from typing import Dict

class Pilar:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        return {
            "Área do Pilar (m²)": area_secao,
            "Carga Aplicada (kN)": self.carga
        }
