import os
import sqlite3
from datetime import datetime

# Definindo os caminhos
origem = r"C:\Users\m1603994\smi\db\banco_smi.db"
destino_base = r"C:\Users\m1603994\backup_db"

# Verifica se o diretório de destino existe, caso contrário, cria
if not os.path.exists(destino_base):
    os.makedirs(destino_base)

# Obtém a data e hora atual no formato DD-MM-AAAA_HH-MM
data_hora_atual = datetime.now().strftime("%d-%m-%Y_%H-%M")

# Cria o nome do arquivo de backup com a data e hora
nome_arquivo_backup = f"banco_smi_{data_hora_atual}.db"
destino_completo = os.path.join(destino_base, nome_arquivo_backup)

# Realiza o backup usando o comando .backup do SQLite
try:
    # Conecta ao banco de dados de origem
    conexao_origem = sqlite3.connect(origem)
    
    # Abre uma conexão com o arquivo de backup (destino)
    conexao_destino = sqlite3.connect(destino_completo)
    
    # Executa o comando .backup
    with conexao_destino:
        conexao_origem.backup(conexao_destino)
    
    print(f"Backup realizado com sucesso! Arquivo salvo como: {nome_arquivo_backup}")

except FileNotFoundError:
    print("Erro: O arquivo de origem não foi encontrado.")
except PermissionError:
    print("Erro: Permissão negada ao acessar os arquivos.")
except sqlite3.Error as e:
    print(f"Erro ao realizar o backup do banco de dados: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    # Fecha as conexões com os bancos de dados
    if 'conexao_origem' in locals():
        conexao_origem.close()
    if 'conexao_destino' in locals():
        conexao_destino.close()