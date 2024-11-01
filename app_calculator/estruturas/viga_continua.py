# Código para a classe VigaContinua
from typing import Dict

class VigaContinua:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura da Viga Contínua (m)": self.largura,
            "Altura da Viga Contínua (m)": self.altura
        }
