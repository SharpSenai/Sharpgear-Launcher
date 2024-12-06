import os
import requests
import subprocess
from pyunpack import Archive

def download_file(url, save_path):

    response = requests.get(url, stream=True)
    response.raise_for_status() 
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Arquivo baixado em: {save_path}")

def extract_rar(rar_path, extract_to):

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    Archive(rar_path).extractall(extract_to)
    print(f"Arquivos extraídos para: {extract_to}")

def run_executable(folder_path, executable_name):

    executable_path = os.path.join(folder_path, executable_name)
    if os.path.exists(executable_path):
        subprocess.Popen(executable_path, shell=True)
        print(f"Executando: {executable_name}")
    else:
        print(f"Executável {executable_name} não encontrado em {folder_path}")

# URL do arquivo .rar
url = "https://exemplo.com/arquivo.rar"
rar_file_path = "arquivo.rar"
extract_folder = "extraido"
executable_name = "programa.exe"

# Etapas do processo
download_file(url, rar_file_path)
extract_rar(rar_file_path, extract_folder)
run_executable(extract_folder, executable_name)
