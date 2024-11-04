from app_calculator.estruturas import (
    Pilar, Viga, Laje, Arco, Trelica, VigaContinua, Flecha, Detalhamento
)
from app_calculator.fundacoes import (
    SapataRigida, SapataCorrida, Bloco, TubulaoCeuAberto,
    TubulaoArComprimido, EstacaHeliceContinua, Radier
)
from app_calculator.config import MENSAGEM_OPCAO_INVALIDA


def calcular_pre_dimensionamento():
    print("\n--- Cálculo de Pré-Dimensionamento ---")
    print("Opções de tipo de peça disponíveis: pilar, viga, laje, fundacao, arco, trelica, viga_continua, flecha, detalhamento")
    tipo_peca = input("Digite o tipo de peça desejado: ").strip().lower()

    if tipo_peca not in ["pilar", "viga", "laje", "fundacao", "arco", "trelica", "viga_continua", "flecha", "detalhamento"]:
        print(MENSAGEM_OPCAO_INVALIDA)
        return

    try:
        largura = float(input("Digite a largura da peça em metros: "))
        altura = float(input("Digite a altura da peça em metros: "))
        carga = float(input("Digite a carga aplicada em kN: "))
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para as dimensões e carga.")
        return

    if largura <= 0 or altura <= 0 or carga <= 0:
        print("A largura, altura e carga devem ser valores positivos.")
        return

    # Seleção do tipo de fundação
    if tipo_peca == "fundacao":
        escolher_tipo_fundacao(carga, largura, altura)
    else:
        calcular_elemento(tipo_peca, largura, altura, carga)


def calcular_elemento(tipo_peca, largura, altura, carga):
    if tipo_peca == "pilar":
        pilar = Pilar(carga, largura, altura)
        print(pilar.gerar_relatorio())
    elif tipo_peca == "viga":
        comprimento = float(input("Digite o comprimento da viga em metros: "))
        viga = Viga(carga, largura, altura, comprimento)
        print(viga.gerar_relatorio())
    elif tipo_peca == "laje":
        laje = Laje(carga, largura, altura)
        print(laje.gerar_relatorio())
    elif tipo_peca == "arco":
        raio = float(input("Digite o raio do arco em metros: "))
        arco = Arco(carga, largura, altura, raio)
        print(arco.gerar_relatorio())
    elif tipo_peca == "trelica":
        trelica = Trelica(carga, largura, altura)
        print(trelica.gerar_relatorio())
    elif tipo_peca == "viga_continua":
        viga_continua = VigaContinua(carga, largura, altura)
        print(viga_continua.gerar_relatorio())
    elif tipo_peca == "flecha":
        flecha = Flecha(carga, largura, altura)
        print(flecha.gerar_relatorio())
    elif tipo_peca == "detalhamento":
        detalhamento = Detalhamento(carga, largura, altura)
        print(detalhamento.gerar_relatorio())


def escolher_tipo_fundacao(carga, largura, altura):
    print("\n--- Tipos de Fundação ---")
    print("1. Sapata Rígida")
    print("2. Sapata Corrida")
    print("3. Bloco")
    print("4. Tubulão Céu Aberto")
    print("5. Tubulão Sob Ar Comprimido")
    print("6. Estaca Hélice Contínua")
    print("7. Radier")

    escolha = input("Escolha o tipo de fundação: ")

    if escolha == "1":
        sapata = SapataRigida(carga, largura, altura)
        print(sapata.gerar_relatorio())
    elif escolha == "2":
        sapata_corrida = SapataCorrida(carga, largura, altura)
        print(sapata_corrida.gerar_relatorio())
    elif escolha == "3":
        bloco = Bloco(carga, largura, altura)
        print(bloco.gerar_relatorio())
    elif escolha == "4":
        tubulao_ceu_aberto = TubulaoCeuAberto(carga, largura, altura)
        print(tubulao_ceu_aberto.gerar_relatorio())
    elif escolha == "5":
        tubulao_ar_comprimido = TubulaoArComprimido(carga, largura, altura)
        print(tubulao_ar_comprimido.gerar_relatorio())
    elif escolha == "6":
        estaca_helice_continua = EstacaHeliceContinua(carga, largura, altura)
        print(estaca_helice_continua.gerar_relatorio())
    elif escolha == "7":
        radier = Radier(carga, largura, altura)
        print(radier.gerar_relatorio())
    else:
        print(MENSAGEM_OPCAO_INVALIDA)
