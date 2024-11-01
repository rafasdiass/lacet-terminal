# Código para a classe Arco
import math
from typing import Dict

class Arco:
    def __init__(self, carga: float, largura: float, altura: float, raio: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.raio = raio

    def gerar_relatorio(self) -> Dict[str, float]:
        momento_fletor = (self.carga * self.raio) / 2
        return {
            "Raio do Arco (m)": self.raio,
            "Momento Fletor (kN.m)": momento_fletor,
            "Carga Aplicada (kN)": self.carga
        }
