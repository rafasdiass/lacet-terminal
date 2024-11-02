from .tipos_solo import SoloArenoso, SoloArgiloso, SoloRochoso
from .camadas_solo import CamadaSolo

class SoloManager:
    @staticmethod
    def criar_solo(tipo, **kwargs):
        if tipo == "arenoso":
            return SoloArenoso(**kwargs)
        elif tipo == "argiloso":
            return SoloArgiloso(**kwargs)
        elif tipo == "rochoso":
            return SoloRochoso(**kwargs)
        else:
            raise ValueError(f"Tipo de solo '{tipo}' não reconhecido.")

    @staticmethod
    def criar_camada(tipo, profundidade, **kwargs):
        solo = SoloManager.criar_solo(tipo, **kwargs)
        return CamadaSolo(solo, profundidade)
