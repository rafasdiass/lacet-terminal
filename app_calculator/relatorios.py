# app_calculator/relatorios.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime

def gerar_relatorio_pdf():
    print("\n--- Geração de Relatório em PDF ---")
    nome_arquivo = f"relatorio_calculo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    c.setTitle("Relatório de Cálculo Estrutural - LCT Calculator")
    
    # Título
    c.drawString(100, 800, "Relatório de Cálculo Estrutural")
    c.drawString(100, 780, "LCT Calculator")

    # Detalhes do cálculo
    c.drawString(100, 740, "Detalhes do Cálculo:")
    c.drawString(100, 720, "Material: Concreto")
    c.drawString(100, 700, "Resistência característica: 25 MPa")
    c.drawString(100, 680, "Carga aplicada: 500 kN")
    c.drawString(100, 660, "Área da seção transversal: 300 cm²")
    c.drawString(100, 640, "Tensão calculada: 16.67 MPa")
    
    # Resultados e observações
    c.drawString(100, 600, "Resultado:")
    c.drawString(100, 580, "A tensão está dentro dos limites aceitáveis para o concreto.")
    
    # Finalização
    c.drawString(100, 520, "Data de geração do relatório: " + str(datetime.datetime.now()))
    c.drawString(100, 500, "-------------------------------")
    c.drawString(100, 480, "Assinatura do engenheiro responsável")

    # Salva o arquivo PDF
    c.save()
    print(f"Relatório gerado com sucesso: {nome_arquivo}")
