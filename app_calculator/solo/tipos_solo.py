class SoloArenoso:
    def __init__(self, capacidade_carga=150, coeficiente_atrito=0.5, compressibilidade=1.2):
        self.capacidade_carga = capacidade_carga
        self.coeficiente_atrito = coeficiente_atrito
        self.compressibilidade = compressibilidade

class SoloArgiloso:
    def __init__(self, capacidade_carga=100, coeficiente_atrito=0.3, compressibilidade=1.5):
        self.capacidade_carga = capacidade_carga
        self.coeficiente_atrito = coeficiente_atrito
        self.compressibilidade = compressibilidade

class SoloRochoso:
    def __init__(self, capacidade_carga=300, coeficiente_atrito=0.7, compressibilidade=0.8):
        self.capacidade_carga = capacidade_carga
        self.coeficiente_atrito = coeficiente_atrito
        self.compressibilidade = compressibilidade
