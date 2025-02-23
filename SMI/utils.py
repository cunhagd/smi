import re
import psycopg2

# Configuração da string de conexão com o banco de dados PostgreSQL
DB_HOST = "ethereally-engrossed-springbok.data-1.use1.tembo.io"
DB_PORT = 5432
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "TEit6gBw1SCPAQWY"

def filtrar_keywords(corpo_noticia, debug=False):
    """
    Filtra palavras-chave obrigatórias e adicionais no corpo da notícia.
    """
    try:
        # Conectar ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

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

        # Verificar quais palavras-chave foram encontradas
        palavras_obrigatorias_encontradas = [
            palavra for palavra in palavras_obrigatorias if encontrar_palavra(palavra, corpo_noticia)
        ]
        palavras_adicionais_encontradas = [
            palavra for palavra in palavras_adicionais if encontrar_palavra(palavra, corpo_noticia)
        ]

        # Retornar resultado
        if debug:
            return {
                "obrigatorias": palavras_obrigatorias_encontradas,
                "adicionais": palavras_adicionais_encontradas
            }
        return len(palavras_obrigatorias_encontradas) > 0 and len(palavras_adicionais_encontradas) > 0

    except Exception as e:
        print(f"Erro ao filtrar palavras-chave: {e}")
        return False if not debug else {"obrigatorias": [], "adicionais": []}

    finally:
        # Fechar a conexão com o banco de dados
        if 'conn' in locals():
            conn.close()