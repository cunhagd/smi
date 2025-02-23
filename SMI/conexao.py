import psycopg2
from psycopg2 import OperationalError

def conectar_banco(host, port, database, user, password):
    """Função para conectar ao banco de dados PostgreSQL."""
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        print(f"Conexão bem-sucedida ao banco de dados: {database}!")
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados {database}: {e}")
        return None

def listar_tabelas(conn):
    """Função para listar todas as tabelas no banco de dados, excluindo tabelas do sistema."""
    try:
        with conn.cursor() as cursor:
            # Listar todas as tabelas no schema public, excluindo as tabelas do sistema
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_type = 'BASE TABLE'
            """)
            tables = cursor.fetchall()
            
            print("Tabelas encontradas no banco de dados 'postgres':")
            for table in tables:
                print(f"  - {table[0]}")
    
    except Exception as e:
        print(f"Erro ao listar as tabelas: {e}")

def listar_tabelas_postgres():
    # Configurações do banco de dados PostgreSQL
    DB_HOST = "ethereally-engrossed-springbok.data-1.use1.tembo.io"
    DB_PORT = 5432
    DB_NAME = "postgres"
    DB_USER = "postgres"
    DB_PASSWORD = "TEit6gBw1SCPAQWY"
    
    conn = conectar_banco(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)
    
    if conn is not None:
        try:
            listar_tabelas(conn)
        except Exception as e:
            print(f"Erro ao executar listagem de tabelas: {e}")
        finally:
            conn.close()
            print("Conexão ao banco de dados fechada.")
    else:
        print("Não foi possível estabelecer a conexão para listar as tabelas.")

if __name__ == "__main__":
    listar_tabelas_postgres()