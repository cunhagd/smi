import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('db/banco_smi.db')
cursor = conn.cursor()

# Deletar a tabela antiga e criar a nova tabela
cursor.execute("""
    DROP TABLE IF EXISTS crawler;
""")
cursor.execute("""
    CREATE TABLE crawler (
        id INTEGER PRIMARY KEY,
        categoria TEXT
    );
""")

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()
