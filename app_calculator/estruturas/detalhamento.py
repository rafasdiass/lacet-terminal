# Código para a classe Detalhamento
from typing import Dict

class Detalhamento:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        return {
            "Carga Aplicada (kN)": self.carga,
            "Largura do Detalhamento (m)": self.largura,
            "Altura do Detalhamento (m)": self.altura
        }
