# Código para a classe Trelica
from typing import Dict

class Trelica:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Treliça (m)": self.largura,
            "Altura da Treliça (m)": self.altura
        }
