import re

def verificar_palavras_chave(texto, palavras_adicionais, palavras_obrigatorias):
    palavras_obrigatorias_encontradas = []
    palavras_adicionais_encontradas = []
    valido = False

    # Função auxiliar para verificar e normalizar siglas
    def normalizar_sigla(palavra):
        # Se a palavra contém 2 ou mais letras maiúsculas seguidas, consideramos como sigla
        if re.search(r'[A-Z]{2,}', palavra):  # Regex para detectar 2 ou mais maiúsculas consecutivas
            return palavra.upper()  # Força para maiúscula
        else:
            return palavra.lower()  # Normaliza para minúscula caso contrário
    
    # Verificar palavras obrigatórias
    for palavra in palavras_obrigatorias:
        palavra_normalizada = normalizar_sigla(palavra)  # Normaliza a palavra para a verificação
        if palavra_normalizada in texto.lower():  # Verifica em minúsculas no texto
            palavras_obrigatorias_encontradas.append(palavra)
            valido = True  # Pelo menos uma palavra obrigatória foi encontrada

    # Verificar palavras adicionais, mas só se já tiver encontrado uma palavra obrigatória
    if valido:
        for palavra in palavras_adicionais:
            palavra_normalizada = normalizar_sigla(palavra)  # Normaliza a palavra para a verificação
            if palavra_normalizada in texto.lower():  # Verifica em minúsculas no texto
                palavras_adicionais_encontradas.append(palavra)
        
    # Validar se existe ao menos uma palavra adicional
    if valido and len(palavras_adicionais_encontradas) > 0:
        return True, palavras_obrigatorias_encontradas, palavras_adicionais_encontradas
    else:
        return False, palavras_obrigatorias_encontradas, palavras_adicionais_encontradas
