import sqlite3
from db.automate.notin import valores  # Importa a lista 'valores' do arquivo notin.py

# Função para conectar ao banco de dados e inserir os valores
def salvar_valores_no_banco():
    # Caminho para o banco de dados
    caminho_banco = r"db\banco_smi.db"

    # Conectar ao banco de dados (ou criar se não existir)
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    try:
        # Criar a tabela 'crawler' se ela não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crawler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT NOT NULL
            )
        ''')

        # Inserir cada valor da lista 'valores' na tabela 'crawler'
        for valor in valores:
            cursor.execute('INSERT INTO crawler (categoria) VALUES (?)', (valor,))

        # Confirmar as alterações no banco de dados
        conexao.commit()
        print(f"{len(valores)} valores foram salvos na tabela 'crawler'.")

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        conexao.close()

if __name__ == "__main__":
    salvar_valores_no_banco()