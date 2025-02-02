import sqlite3
import json  # Usado para serializar listas em strings JSON

def conectar_bd():
    """Conecta ao banco de dados e retorna a conexão e o cursor."""
    conn = sqlite3.connect('db/banco_smi.db')
    cursor = conn.cursor()
    return conn, cursor

def carregar_palavras_chave(tipo):
    """Carrega as palavras-chave do banco de dados."""
    conn, cursor = conectar_bd()
    cursor.execute('SELECT palavra FROM palavras_chave WHERE tipo = ?', (tipo,))
    palavras = [row[0] for row in cursor.fetchall()]
    conn.close()
    return palavras

def obter_pontos_portal(portal_id):
    """Obtém a pontuação do portal."""
    conn, cursor = conectar_bd()
    cursor.execute("SELECT pontos FROM portais WHERE id = ?", (portal_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0

def salvar_noticia(data, name, titulo, corpo, link, autor, pontos, palavras_adicionais, palavras_obrigatorias):
    """Salva a notícia no banco de dados, mas verifica se a URL já existe antes."""
    
    # Verifica se a URL já existe no banco de dados
    conn, cursor = conectar_bd()
    cursor.execute("SELECT 1 FROM noticias WHERE link = ?", (link,))
    if cursor.fetchone():
        conn.close()
        print(f"A notícia com o link {link} já existe. Ignorando a duplicata.")
        return  # Não salva a notícia se a URL já estiver no banco
    
    # Serializando as listas de palavras-chave para armazenamento no banco
    palavras_adicionais_str = ', '.join(palavras_adicionais)
    palavras_obrigatorias_str = ', '.join(palavras_obrigatorias)
    
    # Insere a notícia no banco
    cursor.execute("""
        INSERT INTO noticias (data, portal, titulo, corpo, link, autor, pontos, adicionais, obrigatorias)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (data, name, titulo, corpo, link, autor, pontos, palavras_adicionais_str, palavras_obrigatorias_str))
    
    conn.commit()
    conn.close()
    print(f"Notícia '{titulo}' salva com sucesso.")
