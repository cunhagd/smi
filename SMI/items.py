import sqlite3
from datetime import datetime
import re

# Caminho do banco de dados
DB_PATH = r"db\banco_smi.db"


# Função para buscar URLs associadas a um apelido específico
def buscar_urls(db_path, apelido):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Consulta SQL para buscar todas as URLs associadas ao apelido
        cursor.execute("SELECT rastreio FROM portais WHERE apelido = ?", (apelido,))
        resultados = cursor.fetchall()
        
        # Extrair as URLs da lista de tuplas retornada pelo fetchall
        urls = [resultado[0] for resultado in resultados]
        
        return urls
    
    except Exception as e:
        print(f"Erro ao buscar URLs para o apelido '{apelido}': {e}")
        return []
    
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

def buscar_apelido(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Consulta SQL para buscar todos os apelidos na tabela 'portais'
        cursor.execute("SELECT apelido FROM portais WHERE nome = ?", (name,))
        resultados = cursor.fetchall()
        
        # Extrair os apelidos da lista de tuplas retornada pelo fetchall
        apelidos = [resultado[0] for resultado in resultados]
        return apelidos
    
    except Exception as e:
        print(f"Erro ao buscar apelidos: {e}")
        return []
    
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

def filtar_data(data):
    # Formato da data: DD/MM/AAAA
    try:
        dia, mes, ano = map(int, data.split('/'))
        return datetime.date(ano, mes, dia)
    except Exception as e:
        print(f"Erro ao converter data: {e}")
        return None
    
def buscar_categorias():
    # Caminho para o banco de dados
    caminho_banco = "db/banco_smi.db"

    try:
        # Conectar ao banco de dados
        conexao = sqlite3.connect(caminho_banco)
        cursor = conexao.cursor()

        # Consultar todos os valores da coluna 'categoria'
        cursor.execute("SELECT categoria FROM crawler")
        resultados = cursor.fetchall()

        # Extrair os valores da lista de tuplas retornada pelo fetchall()
        categorias = [resultado[0] for resultado in resultados]

        print(f"{len(categorias)} categorias encontradas na tabela 'crawler'.")
        return categorias

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []

    finally:
        # Fechar a conexão com o banco de dados
        if 'conexao' in locals():
            conexao.close()


def seletor_corpo(db_path, name):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Consulta SQL para buscar o seletor associado ao nome do portal
        cursor.execute("SELECT sel_corpo FROM portais WHERE nome = ?", (name,))
        resultado = cursor.fetchone()  # Retorna apenas uma linha
        
        # Verifica se há um resultado
        if resultado:
            return resultado[0]  # Retorna o seletor CSS
        else:
            print(f"Nenhum seletor encontrado para o nome '{name}'")
            return None
    
    except Exception as e:
        print(f"Erro ao buscar seletor para o nome '{name}': {e}")
        return None
    
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

def filtrar_keywords(db_path, corpo_noticia, debug=False):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Consulta SQL para buscar palavras-chave obrigatórias e adicionais
        cursor.execute("SELECT palavra, tipo FROM palavras_chave")
        resultados = cursor.fetchall()
        
        # Separar as palavras-chave em duas listas
        palavras_obrigatorias = [row[0] for row in resultados if row[1] == 'obrigatoria']
        palavras_adicionais = [row[0] for row in resultados if row[1] == 'adicional']
        
        # Função auxiliar para verificar se uma palavra é uma sigla (duas letras maiúsculas seguidas)
        def is_sigla(palavra):
            return any(char.isupper() and palavra[i + 1].isupper() for i, char in enumerate(palavra[:-1]))
        
        # Função auxiliar para verificar se uma palavra-chave existe no corpo da notícia
        def encontrar_palavra(palavra, texto):
            if is_sigla(palavra):
                # Para siglas, usar regex para garantir correspondência exata
                padrao = r'\b' + re.escape(palavra) + r'\b'
                return bool(re.search(padrao, texto))
            else:
                # Para palavras normais, verificar case-insensitive
                padrao = r'\b' + re.escape(palavra.lower()) + r'\b'
                return bool(re.search(padrao, texto.lower()))
        
        # Debug: Imprimir todas as palavras-chave para verificação
        print(f"Palavras-chave obrigatórias: {palavras_obrigatorias}")
        print(f"Palavras-chave adicionais: {palavras_adicionais}")
        
        # Verificar quais palavras-chave foram encontradas
        palavras_obrigatorias_encontradas = [
            palavra for palavra in palavras_obrigatorias if encontrar_palavra(palavra, corpo_noticia)
        ]
        palavras_adicionais_encontradas = [
            palavra for palavra in palavras_adicionais if encontrar_palavra(palavra, corpo_noticia)
        ]
        
        # Debug: Imprimir palavras encontradas para verificação
        print(f"Palavras obrigatórias encontradas: {palavras_obrigatorias_encontradas}")
        print(f"Palavras adicionais encontradas: {palavras_adicionais_encontradas}")
        
        # Verificar se a notícia atende às regras
        tem_obrigatoria = len(palavras_obrigatorias_encontradas) > 0
        tem_adicional = len(palavras_adicionais_encontradas) > 0
        
        # Retornar resultado
        if debug:
            return {
                "obrigatorias": palavras_obrigatorias_encontradas,
                "adicionais": palavras_adicionais_encontradas
            }
        return tem_obrigatoria and tem_adicional
    
    except Exception as e:
        print(f"Erro ao filtrar palavras-chave: {e}")
        return False if not debug else {"obrigatorias": [], "adicionais": []}
    
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

    