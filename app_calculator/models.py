from django.db import models

class Estrutura(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    largura = models.FloatField()
    altura = models.FloatField()
    carga = models.FloatField()
    comprimento = models.FloatField(null=True, blank=True)
    raio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def calcular_area(self):
        """Calcula a área da seção transversal."""
        return self.largura * self.altura

    def calcular_tensao(self):
        """Calcula a tensão aplicada no elemento."""
        if self.calcular_area() > 0:
            return self.carga / self.calcular_area()
        return None
