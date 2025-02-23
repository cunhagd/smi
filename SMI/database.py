import psycopg2
from datetime import datetime
import re
import os

# Configurações do banco de dados PostgreSQL
DB_HOST = "ethereally-engrossed-springbok.data-1.use1.tembo.io"
DB_PORT = 5432
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "TEit6gBw1SCPAQWY"

def conectar_banco():
    """Função para conectar ao banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def buscar_urls(apelido):
    conn = conectar_banco()
    if not conn:
        return []
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT rastreio FROM portais WHERE apelido = %s", (apelido,))
        resultados = cursor.fetchall()
        return [resultado[0] for resultado in resultados]
    except Exception as e:
        print(f"Erro ao buscar URLs para o apelido '{apelido}': {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_apelido(name):
    conn = conectar_banco()
    if not conn:
        return []
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT apelido FROM portais WHERE nome = %s", (name,))
        resultados = cursor.fetchall()
        return [resultado[0] for resultado in resultados]
    except Exception as e:
        print(f"Erro ao buscar apelidos: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def buscar_pontos(name):
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT pontos FROM portais WHERE nome = %s", (name,))
        resultados = cursor.fetchall()
        return resultados[0][0] if resultados else None
    except Exception as e:
        print(f"Erro ao buscar pontos: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def buscar_abrangencia(name):
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT abrangencia FROM portais WHERE nome = %s", (name,))
        resultados = cursor.fetchall()
        return resultados[0][0] if resultados else None
    except Exception as e:
        print(f"Erro ao buscar abrangência: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def buscar_categorias():
    conn = conectar_banco()
    if not conn:
        return []
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT categoria FROM crawler")
        resultados = cursor.fetchall()
        categorias = [resultado[0] for resultado in resultados]
        print(f"{len(categorias)} categorias encontradas na tabela 'crawler'.")
        return categorias
    except Exception as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def seletor_corpo(name):
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT sel_corpo FROM portais WHERE nome = %s", (name,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao buscar seletor para o nome '{name}': {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def seletor_autor(name):
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT sel_autor FROM portais WHERE nome = %s", (name,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao buscar seletor para o nome '{name}': {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def testar_permissoes():
    conn = conectar_banco()
    if not conn:
        print("Falha na conexão com o banco de dados.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")  # Consulta trivial para testar permissão de leitura
            resultado = cursor.fetchone()
            if resultado and resultado[0] == 1:
                print("Permissão de leitura confirmada.")
            else:
                print("Erro ao executar consulta simples.")
    except psycopg2.Error as e:
        print(f"Erro ao testar permissões: {e}")
    finally:
        conn.close()

testar_permissoes()