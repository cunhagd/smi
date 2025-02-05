import re
import sqlite3


def filtrar_keywords(db_path, corpo_noticia, debug=False):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT palavra, tipo FROM palavras_chave")
        resultados = cursor.fetchall()
        palavras_obrigatorias = [row[0] for row in resultados if row[1] == 'obrigatoria']
        palavras_adicionais = [row[0] for row in resultados if row[1] == 'adicional']

        def is_sigla(palavra):
            return any(char.isupper() and palavra[i + 1].isupper() for i, char in enumerate(palavra[:-1]))

        def encontrar_palavra(palavra, texto):
            if is_sigla(palavra):
                padrao = r'\b' + re.escape(palavra) + r'\b'
                return bool(re.search(padrao, texto))
            else:
                padrao = r'\b' + re.escape(palavra.lower()) + r'\b'
                return bool(re.search(padrao, texto.lower()))

        palavras_obrigatorias_encontradas = [
            palavra for palavra in palavras_obrigatorias if encontrar_palavra(palavra, corpo_noticia)
        ]
        palavras_adicionais_encontradas = [
            palavra for palavra in palavras_adicionais if encontrar_palavra(palavra, corpo_noticia)
        ]

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
        conn.close()