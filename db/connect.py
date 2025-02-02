import sqlite3

def criar_conexao(db_path='db/banco_smi.db'):
    """Estabelece a conexão com o banco de dados SQLite. Cria o arquivo se não existir."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def criar_tabelas(conn):
    """Cria as tabelas necessárias no banco de dados."""
    try:
        with conn:
            cursor = conn.cursor()
            
            # Criar a tabela 'noticias'
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS noticias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,       -- Data da publicação
                    portal TEXT NOT NULL,     -- Nome do veículo
                    titulo TEXT NOT NULL,     -- Título da matéria
                    corpo TEXT NOT NULL,      -- Corpo da matéria
                    link TEXT NOT NULL UNIQUE,-- Link da matéria
                    autor TEXT,               -- Autor da matéria (pode ser nulo)
                    pontos INTEGER,           -- Pontuação do portal
                    keywords TEXT             -- Palavras-chave (texto livre ou separado por vírgula)
                )
            ''')
            
            # Criar a tabela 'portais'
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS portais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,        -- Nome do portal
                    url TEXT NOT NULL UNIQUE,  -- URL do portal
                    abrangencia TEXT,          -- Abrangência (ex: Regional/Nacional/Local)
                    prioridade TEXT,           -- Prioridade da fonte (Baixa/Média/Alta)
                    pontos INTEGER,            -- Pontuação do portal
                    apelido TEXT               -- Chave para o nome do portal
                )
            ''')
            
            print("Tabelas 'noticias' e 'portais' criadas ou já existem.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabelas: {e}")
        raise

def criar_tabela_palavras_chave():
    """Cria a tabela de palavras-chave, utilizando a função de conexão."""
    try:
        conn = criar_conexao()  # Usando a função de criar conexão
        cursor = conn.cursor()

        # Criar a tabela de palavras-chave
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS palavras_chave (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,   -- 'obrigatoria' ou 'adicional'
                palavra TEXT NOT NULL UNIQUE
            )
        ''')

        # Commit e fechar a conexão
        conn.commit()
        print("Tabela 'palavras_chave' criada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        conn.close()  # Fechar a conexão após a operação

def main():
    # Criar as tabelas no banco de dados
    conn = criar_conexao()  # Estabelecer conexão com o banco
    # criar_tabelas(conn)  # Criar as tabelas principais (noticias, portais)
    criar_tabela_palavras_chave()  # Criar a tabela de palavras-chave

if __name__ == '__main__':
    main()
