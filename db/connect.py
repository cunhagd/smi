import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('db/banco_smi.db')
cursor = conn.cursor()

# Deletar a tabela antiga e criar a nova tabela
cursor.execute("""
    DROP TABLE IF EXISTS noticias;
""")
cursor.execute("""
    CREATE TABLE noticias (
        id INTEGER PRIMARY KEY,
        data TEXT,
        portal TEXT,
        titulo TEXT,
        corpo TEXT,
        link TEXT,
        autor TEXT,
        pontos INTEGER,
        adicionais TEXT,
        obrigatorias TEXT
    );
""")

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()
