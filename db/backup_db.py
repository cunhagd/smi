import os
import shutil
from datetime import datetime

# Definindo os caminhos
origem = r"C:\Users\m1603994\smi\db\banco_smi.db"
destino_base = r"C:\Users\m1603994\smi\db\backup_db"

# Verifica se o diretório de destino existe, caso contrário, cria
if not os.path.exists(destino_base):
    os.makedirs(destino_base)

# Obtém a data e hora atual no formato DD-MM-AAAA_HH-MM
data_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M")

# Cria o nome do arquivo de backup com a data e hora
nome_arquivo_backup = f"banco_smi_{data_hora_atual}.db"
destino_completo = os.path.join(destino_base, nome_arquivo_backup)

# Copia o arquivo para o diretório de backup
try:
    shutil.copy2(origem, destino_completo)
    print(f"Backup realizado com sucesso! Arquivo salvo como: {nome_arquivo_backup}")
except FileNotFoundError:
    print("Erro: O arquivo de origem não foi encontrado.")
except PermissionError:
    print("Erro: Permissão negada ao acessar os arquivos.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")