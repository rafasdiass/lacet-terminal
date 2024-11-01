# Código para a classe Flecha
from typing import Dict

class Flecha:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Flecha (m)": self.largura,
            "Altura da Flecha (m)": self.altura
        }
