import sqlite3
import psycopg2
from psycopg2 import sql

# Função para criar o banco de dados se ele não existir
def create_database_if_not_exists(conn_params, db_name):
    try:
        # Conecte-se ao banco de dados padrão 'postgres'
        temp_conn = psycopg2.connect(
            dbname="postgres",
            user=conn_params["user"],
            password=conn_params["password"],
            host=conn_params["host"],
            port=conn_params["port"]
        )
        temp_conn.autocommit = True  # Necessário para criar um banco de dados
        temp_cursor = temp_conn.cursor()

        # Verifique se o banco de dados já existe
        temp_cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (db_name,))
        exists = temp_cursor.fetchone()

        if not exists:
            print(f"Criando banco de dados '{db_name}'...")
            temp_cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        else:
            print(f"Banco de dados '{db_name}' já existe.")

        temp_cursor.close()
        temp_conn.close()
    except Exception as e:
        print(f"Erro ao criar ou verificar o banco de dados: {e}")
        raise

# Parâmetros de conexão com o PostgreSQL
pg_conn_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "TEit6gBw1SCPAQWY",
    "host": "ethereally-engrossed-springbok.data-1.use1.tembo.io",
    "port": 5432
}

# Crie o banco de dados se ele não existir
create_database_if_not_exists(pg_conn_params, "banco_smi")

# Conexão com o SQLite
sqlite_conn = sqlite3.connect(r'C:\Users\m1603994\teste_smi\smi\db\banco_smi.db')
sqlite_cursor = sqlite_conn.cursor()

# Conexão com o PostgreSQL (agora o banco de dados 'banco_smi' existe)
pg_conn = psycopg2.connect(**pg_conn_params)
pg_cursor = pg_conn.cursor()

# Obtenha as tabelas do SQLite
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = sqlite_cursor.fetchall()

# Filtra a tabela 'sqlite_sequence', pois ela é específica do SQLite
tables = [table for table in tables if table[0] != "sqlite_sequence"]

# Função para mapear tipos SQLite para PostgreSQL
def map_sqlite_to_postgres_type(sqlite_type):
    type_mapping = {
        "INTEGER": "INTEGER",
        "TEXT": "TEXT",
        "REAL": "DOUBLE PRECISION",
        "BLOB": "BYTEA",
        "NUMERIC": "NUMERIC",
        "BOOLEAN": "BOOLEAN"
    }
    return type_mapping.get(sqlite_type.upper(), "TEXT")  # Default to TEXT if type is unknown

# Cria as tabelas no PostgreSQL
for table_name in tables:
    table_name = table_name[0]
    print(f"Criando tabela: {table_name}")

    # Obtenha as informações das colunas da tabela SQLite
    sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
    columns_info = sqlite_cursor.fetchall()

    # Construa a instrução CREATE TABLE para PostgreSQL
    columns_definitions = []
    for column in columns_info:
        col_name = column[1]
        col_type = map_sqlite_to_postgres_type(column[2])
        is_primary_key = "PRIMARY KEY" if column[5] else ""
        columns_definitions.append(f"{col_name} {col_type} {is_primary_key}".strip())

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_definitions)});"
    pg_cursor.execute(create_table_query)

# Migra os dados para o PostgreSQL
for table_name in tables:
    table_name = table_name[0]
    print(f"Migrando tabela: {table_name}")

    # Obtenha os dados da tabela SQLite
    sqlite_cursor.execute(f"SELECT * FROM {table_name};")
    rows = sqlite_cursor.fetchall()

    # Obtenha as colunas da tabela SQLite
    sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [col[1] for col in sqlite_cursor.fetchall()]

    # Construa a instrução INSERT para PostgreSQL
    placeholders = ', '.join(['%s'] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"

    # Insira os dados no PostgreSQL
    for row in rows:
        pg_cursor.execute(insert_query, row)

# Confirme as alterações e feche as conexões
pg_conn.commit()
pg_cursor.close()
pg_conn.close()
sqlite_cursor.close()
sqlite_conn.close()

print("Migração concluída!")