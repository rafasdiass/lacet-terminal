class CamadaSolo:
    def __init__(self, tipo_solo, profundidade):
        self.tipo_solo = tipo_solo
        self.profundidade = profundidade

    def obter_dados(self):
        return {
            "tipo": self.tipo_solo.__class__.__name__,
            "capacidade_carga": self.tipo_solo.capacidade_carga,
            "coeficiente_atrito": self.tipo_solo.coeficiente_atrito,
            "compressibilidade": self.tipo_solo.compressibilidade,
            "profundidade": self.profundidade
        }
