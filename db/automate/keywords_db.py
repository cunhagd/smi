import sqlite3
import db.automate.keywords as keywords  # Importa o módulo com as palavras-chave

def criar_conexao(db_path='db/banco_smi.db'):
    """Estabelece a conexão com o banco de dados SQLite. Cria o arquivo se não existir."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def inserir_palavras_chave(conn, tipo, palavras):
    """Insere as palavras-chave no banco de dados, verificando se já não existem."""
    cursor = conn.cursor()
    for palavra in palavras:
        try:
            # Verifica se a palavra já existe no banco
            cursor.execute('''SELECT id FROM palavras_chave WHERE tipo = ? AND palavra = ?''', (tipo, palavra))
            result = cursor.fetchone()
            
            # Se a palavra não existe, insere no banco de dados
            if not result:
                cursor.execute('''INSERT INTO palavras_chave (tipo, palavra) VALUES (?, ?)''', (tipo, palavra))
                print(f"Palavra '{palavra}' inserida com sucesso.")
            else:
                print(f"Palavra '{palavra}' já existe no banco.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir a palavra '{palavra}': {e}")

    # Commit para garantir que as inserções sejam salvas no banco
    conn.commit()

def salvar_palavras_chave():
    """Função principal para salvar as palavras obrigatórias e adicionais no banco de dados."""
    conn = criar_conexao()  # Conectar ao banco de dados
    try:
        # Inserir palavras obrigatórias
        inserir_palavras_chave(conn, 'obrigatoria', keywords.palavras_obrigatorias)
        
        # Inserir palavras adicionais
        inserir_palavras_chave(conn, 'adicional', keywords.palavras_adicionais)
    finally:
        conn.close()  # Fechar a conexão com o banco

if __name__ == '__main__':
    salvar_palavras_chave()
