import sqlite3
import requests

# Caminho do banco de dados
DB_PATH = r"db\banco_smi.db"

# Função para verificar se uma URL possui um arquivo robots.txt válido
def verificar_robots_txt(url):
    try:
        # Construir a URL completa para o arquivo robots.txt
        if not url.startswith("http"):
            url = "https://" + url  # Garantir que a URL tenha o protocolo HTTPS
        robots_url = f"{url}robots.txt"
        
        # Fazer uma requisição HTTP para verificar o arquivo robots.txt
        response = requests.get(robots_url, timeout=5)
        
        if response.status_code == 200:
            return True, robots_url  # O arquivo existe e é válido
        else:
            return False, None  # O arquivo não foi encontrado ou não é acessível
    except Exception:
        return False, None  # Erro ao acessar a URL (timeout, conexão falhou, etc.)

# Função principal para analisar as URLs e gerar o relatório
def analisar_urls():
    # Conectar ao banco de dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Consultar todas as URLs da coluna 'url' na tabela 'portais'
    cursor.execute("SELECT url FROM portais")
    urls = [row[0] for row in cursor.fetchall()]
    
    # Fechar a conexão com o banco de dados
    conn.close()
    
    # Inicializar variáveis para o relatório
    links_analisados = 0
    links_com_robots_txt = []
    
    # Verificar cada URL
    for url in urls:
        links_analisados += 1
        print(f"Analisando URL: {url}")
        sucesso, robots_url = verificar_robots_txt(url)
        if sucesso:
            print(f"Encontrado robots.txt: {robots_url}")
            links_com_robots_txt.append(robots_url)
        else:
            print(f"Nenhum robots.txt encontrado para: {url}")
    
    # Gerar o relatório em um arquivo
    with open("analise_robots.txt", "w", encoding="utf-8") as f:
        f.write("=== Relatório de Análise de Robots.txt ===\n\n")
        f.write(f"Total de links analisados: {links_analisados}\n")
        f.write(f"Total de links com robots.txt válido: {len(links_com_robots_txt)}\n\n")
        f.write("Links com robots.txt encontrado:\n")
        for link in links_com_robots_txt:
            f.write(f"- {link}\n")
    
    print("\nRelatório gerado com sucesso no arquivo 'analise_robots.txt'.")

# Executar a função principal
if __name__ == "__main__":
    analisar_urls()