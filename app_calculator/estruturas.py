from typing import Dict
import math

class Pilar:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        tensao_normal = self.carga / area_secao
        momento_resistente = self.carga * self.altura / 4  # Exemplo de momento para pilar centrado

        return {
            "Área do Pilar (m²)": area_secao,
            "Carga Aplicada (kN)": self.carga,
            "Tensão Normal (MPa)": tensao_normal,
            "Momento Resistente (kN.m)": momento_resistente
        }

class Viga:
    def __init__(self, carga: float, largura: float, altura: float, comprimento: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        inercia = (self.largura * self.altura ** 3) / 12
        momento_fletor_maximo = (self.carga * self.comprimento) / 8
        tensao_fletora = momento_fletor_maximo * (self.altura / 2) / inercia

        return {
            "Comprimento da Viga (m)": self.comprimento,
            "Momento Fletor Máximo (kN.m)": momento_fletor_maximo,
            "Área da Seção Transversal (m²)": area_secao,
            "Inércia da Seção (m^4)": inercia,
            "Tensão Fletora Máxima (MPa)": tensao_fletora,
            "Carga Aplicada (kN)": self.carga
        }

class Laje:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area = self.largura * self.altura
        momento_fletor_maximo = self.carga * (self.largura ** 2) / 8
        tensao_fletora = momento_fletor_maximo / (self.altura / 2)

        return {
            "Área da Laje (m²)": area,
            "Momento Fletor Máximo (kN.m)": momento_fletor_maximo,
            "Tensão Fletora (MPa)": tensao_fletora,
            "Carga Aplicada (kN)": self.carga
        }

class Arco:
    def __init__(self, carga: float, largura: float, altura: float, raio: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura
        self.raio = raio

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        momento_fletor = (self.carga * self.raio) / 2
        tensao_fletora = momento_fletor / (self.altura / 2)

        return {
            "Raio do Arco (m)": self.raio,
            "Momento Fletor (kN.m)": momento_fletor,
            "Tensão Fletora (MPa)": tensao_fletora,
            "Área da Seção (m²)": area_secao,
            "Carga Aplicada (kN)": self.carga
        }

class Trelica:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        tensao_tracao = self.carga / area_secao

        return {
            "Largura da Treliça (m)": self.largura,
            "Altura da Treliça (m)": self.altura,
            "Tensão de Tração (MPa)": tensao_tracao,
            "Carga Aplicada (kN)": self.carga
        }

class VigaContinua:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        momento_fletor_maximo = (self.carga * self.largura) / 8
        tensao_fletora_maxima = momento_fletor_maximo / (self.altura / 2)

        return {
            "Largura da Viga Contínua (m)": self.largura,
            "Altura da Viga Contínua (m)": self.altura,
            "Momento Fletor Máximo (kN.m)": momento_fletor_maximo,
            "Tensão Fletora Máxima (MPa)": tensao_fletora_maxima,
            "Carga Aplicada (kN)": self.carga
        }

class Flecha:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        flecha_maxima = (5 * self.carga * self.largura ** 3) / (384 * 210 * area_secao)

        return {
            "Largura da Flecha (m)": self.largura,
            "Altura da Flecha (m)": self.altura,
            "Flecha Máxima (mm)": flecha_maxima,
            "Carga Aplicada (kN)": self.carga
        }

class Detalhamento:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_secao = self.largura * self.altura
        tensao = self.carga / area_secao

        return {
            "Largura do Detalhamento (m)": self.largura,
            "Altura do Detalhamento (m)": self.altura,
            "Tensão (MPa)": tensao,
            "Carga Aplicada (kN)": self.carga
        }

class SapataRigida:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.carga / 150
        tensao_solo = self.carga / area_base

        return {
            "Área Base da Sapata Rígida (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class SapataAssociada:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        tensao_solo = self.carga / area_base

        return {
            "Área Base da Sapata Associada (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class BlocoDeCoroamento:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        tensao_solo = self.carga / area_base

        return {
            "Área Base do Bloco de Coroamento (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class TubulaoCeuAberto:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        tensao_solo = self.carga / area_base

        return {
            "Área Base do Tubulão a Céu Aberto (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class TubulaoSobArComprimido:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        tensao_solo = self.carga / area_base

        return {
            "Área Base do Tubulão com Ar Comprimido (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class EstacaHeliceContinua:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = math.pi * (self.largura / 2) ** 2
        tensao_solo = self.carga / area_base

        return {
            "Área Base da Estaca Hélice Contínua (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class Radier:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        tensao_solo = self.carga / area_base

        return {
            "Área do Radier (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }

class BlocoIsolado:
    def __init__(self, carga: float, largura: float, altura: float):
        self.carga = carga
        self.largura = largura
        self.altura = altura

    def gerar_relatorio(self) -> Dict[str, float]:
        area_base = self.largura * self.altura
        tensao_solo = self.carga / area_base

        return {
            "Área Base do Bloco Isolado (m²)": area_base,
            "Tensão no Solo (kN/m²)": tensao_solo,
            "Carga Aplicada (kN)": self.carga
        }
