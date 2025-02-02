import scrapy
from datetime import datetime

def calcular_data_hoje():
    """Retorna a string com a data de hoje no formato esperado para a URL."""
    hoje = datetime.now()
    return f"/{hoje.year:04}/{hoje.month:02}/{hoje.day:02}/"

def extrair_texto(response, seletor, default="Não encontrado"):
    """Extrai o texto de um seletor CSS, se disponível."""
    elemento = response.css(seletor).get()
    return elemento.strip() if elemento else default

def limpar_autor(autor):
    """Formata corretamente o nome do autor."""
    if autor and autor.lower().startswith("por "):
        return autor[3:].strip()
    return autor if autor else "Autor não encontrado"
