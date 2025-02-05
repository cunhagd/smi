import sqlite3
from datetime import datetime
import re

DB_PATH = r"db\banco_smi.db"

def buscar_urls(db_path, apelido):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT rastreio FROM portais WHERE apelido = ?", (apelido,))
        resultados = cursor.fetchall()
        return [resultado[0] for resultado in resultados]
    except Exception as e:
        print(f"Erro ao buscar URLs para o apelido '{apelido}': {e}")
        return []
    finally:
        conn.close()

def buscar_apelido(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT apelido FROM portais WHERE nome = ?", (name,))
        resultados = cursor.fetchall()
        return [resultado[0] for resultado in resultados]
    except Exception as e:
        print(f"Erro ao buscar apelidos: {e}")
        return []
    finally:
        conn.close()

def buscar_pontos(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT pontos FROM portais WHERE nome = ?", (name,))
        resultados = cursor.fetchall()
        return resultados[0][0] if resultados else None
    except Exception as e:
        print(f"Erro ao buscar pontos: {e}")
        return None
    finally:
        conn.close()

def buscar_abrangencia(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT abrangencia FROM portais WHERE nome = ?", (name,))
        resultados = cursor.fetchall()
        return resultados[0][0] if resultados else None
    except Exception as e:
        print(f"Erro ao buscar abrangência: {e}")
        return None
    finally:
        conn.close()

def buscar_categorias():
    caminho_banco = "db/banco_smi.db"
    try:
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()
        cursor.execute("SELECT categoria FROM crawler")
        resultados = cursor.fetchall()
        categorias = [resultado[0] for resultado in resultados]
        print(f"{len(categorias)} categorias encontradas na tabela 'crawler'.")
        return categorias
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []
    finally:
        if 'conexao' in locals():
            conexao.close()

def seletor_corpo(db_path, name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT sel_corpo FROM portais WHERE nome = ?", (name,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao buscar seletor para o nome '{name}': {e}")
        return None
    finally:
        conn.close()

def seletor_autor(db_path, name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT sel_autor FROM portais WHERE nome = ?", (name,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Erro ao buscar seletor para o nome '{name}': {e}")
        return None
    finally:
        conn.close()