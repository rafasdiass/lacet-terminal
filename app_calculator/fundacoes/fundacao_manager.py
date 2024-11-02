from .barrete import Barrete
from .bloco import Bloco
from .estaca import Estaca
from .estaca_helice_continua import EstacaHeliceContinua
from .radier import Radier
from .sapata_corrida import SapataCorrida
from .sapata_rigida import SapataRigida
from .sapata import Sapata
from .tubulao_ar_comprimido import TubulaoArComprimido
from .tubulao_ceu_aberto import TubulaoCeuAberto
from .tubulao import Tubulao
from app_calculator.solo.solo_manager import SoloManager

class FundacaoManager:
    @staticmethod
    def criar_fundacao(tipo, solo_tipo=None, profundidade=None, **kwargs):
        # Se o tipo de solo foi fornecido, cria uma camada de solo com o SoloManager
        solo = None
        if solo_tipo and profundidade:
            solo = SoloManager.criar_camada(solo_tipo, profundidade)

        # Inicializa a fundação com os dados de solo se disponíveis
        if tipo == "barrete":
            return Barrete(solo=solo, **kwargs)
        elif tipo == "bloco":
            return Bloco(solo=solo, **kwargs)
        elif tipo == "estaca":
            return Estaca(solo=solo, **kwargs)
        elif tipo == "estaca_helice_continua":
            return EstacaHeliceContinua(solo=solo, **kwargs)
        elif tipo == "radier":
            return Radier(solo=solo, **kwargs)
        elif tipo == "sapata_corrida":
            return SapataCorrida(solo=solo, **kwargs)
        elif tipo == "sapata_rigida":
            return SapataRigida(solo=solo, **kwargs)
        elif tipo == "sapata":
            return Sapata(solo=solo, **kwargs)
        elif tipo == "tubulao_ar_comprimido":
            return TubulaoArComprimido(solo=solo, **kwargs)
        elif tipo == "tubulao_ceu_aberto":
            return TubulaoCeuAberto(solo=solo, **kwargs)
        elif tipo == "tubulao":
            return Tubulao(solo=solo, **kwargs)
        else:
            raise ValueError(f"Tipo de fundação '{tipo}' não reconhecido.")
