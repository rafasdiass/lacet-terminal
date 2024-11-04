# Código para a classe Viga
from typing import Dict

class Viga:
    def __init__(self, carga: float, largura: float, altura: float, comprimento: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento

    def gerar_relatorio(self) -> Dict[str, float]:
        momento_fletor = (self.carga * self.comprimento) / 8
        return {
            "Comprimento da Viga (m)": self.comprimento,
            "Momento Fletor (kN.m)": momento_fletor,
            "Carga Aplicada (kN)": self.carga
        }
