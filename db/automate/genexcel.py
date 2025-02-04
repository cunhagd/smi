import sqlite3
import pandas as pd

# Caminho do banco de dados SQLite
DB_PATH = r"db\banco_smi.db"

# Nome do arquivo Excel de saída
EXCEL_FILE = "painel.xlsx"

# Função para exportar todas as tabelas do SQLite para Excel
def exportar_todas_tabelas_para_excel(db_path, excel_file):
    try:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)
        
        # Obter o nome de todas as tabelas no banco de dados
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = [tabela[0] for tabela in cursor.fetchall()]
        
        # Criar um objeto ExcelWriter para salvar várias planilhas
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            for tabela in tabelas:
                # Ler os dados da tabela para um DataFrame
                query = f"SELECT * FROM {tabela}"
                df = pd.read_sql_query(query, conn)
                
                # Salvar a tabela como uma planilha no arquivo Excel
                df.to_excel(writer, sheet_name=tabela, index=False)
        
        print(f"Todas as tabelas foram exportadas com sucesso para '{excel_file}'.")
    
    except Exception as e:
        print(f"Erro ao exportar tabelas: {e}")
    
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Executar a função
if __name__ == "__main__":
    exportar_todas_tabelas_para_excel(DB_PATH, EXCEL_FILE)