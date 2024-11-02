import os

def gerar_installer_cfg():
    # Ler o requirements.txt
    with open('requirements.txt', 'r') as req_file:
        packages = [line.strip().split('==')[0] for line in req_file if line.strip()]

    # Arquivos e diretórios a serem incluídos
    files_to_include = [
        'manage.py',
        'config/',
        'app_calculator/',
        # Adicione outros arquivos ou diretórios necessários
    ]

    # Gerar o installer.cfg
    with open('installer.cfg', 'w') as cfg_file:
        cfg_file.write('[Application]\n')
        cfg_file.write('name=LACET-CALC\n')
        cfg_file.write('version=1.0\n')
        cfg_file.write('entry_point=manage:main\n')
        # Se tiver um ícone, descomente a linha abaixo e ajuste o caminho
        # cfg_file.write('icon=icone.ico\n')

        cfg_file.write('\n[Python]\n')
        cfg_file.write('version=3.9.0\n')
        cfg_file.write('bitness=64\n')

        cfg_file.write('\n[Include]\n')
        cfg_file.write('packages=\n')
        for package in packages:
            cfg_file.write(f'    {package}\n')

        cfg_file.write('pypi_wheels=\n')
        for package in packages:
            cfg_file.write(f'    {package}\n')

        cfg_file.write('files=\n')
        for file in files_to_include:
            cfg_file.write(f'    {file}\n')

if __name__ == "__main__":
    gerar_installer_cfg()
