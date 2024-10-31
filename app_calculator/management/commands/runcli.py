# app_calculator/management/commands/runcli.py

from django.core.management.base import BaseCommand
from app_calculator.cli import run_cli  # Importa a função CLI principal

class Command(BaseCommand):
    help = "Inicia a interface de linha de comando para o LCT Calculator"

    def handle(self, *args, **kwargs):
        run_cli()  # Chama a função principal da CLI
