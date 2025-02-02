import os
import sqlite3

# Caminho do banco de dados
DB_PATH = r"C:\Users\m1603994\SMI\db\banco_smi.db"
BASE_DIR = r"C:\Users\m1603994\SMI\SMI\spiders"

# Conectar ao banco de dados
def get_portais():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ID, nome, url, abrangencia, apelido FROM portais")
    portais = cursor.fetchall()
    conn.close()
    return portais

# Criar estrutura de diretórios
def criar_pasta(abrangencia):
    pasta = os.path.join(BASE_DIR, abrangencia.lower())
    os.makedirs(pasta, exist_ok=True)
    return pasta

# Gerar código base do spider
def gerar_spider_code(id_portal, nome, url, apelido):
    return f'''import scrapy

class {apelido.capitalize()}Spider(scrapy.Spider):
    name = "{nome}"
    ID = {id_portal}
    allowed_domains = ["{url.replace('https://', '').replace('http://', '').split('/')[0]}"]
    start_urls = ["{url}"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
'''

# Criar spiders automaticamente
def criar_spiders():
    os.makedirs(BASE_DIR, exist_ok=True)  # Garante que a pasta spiders principal seja criada
    portais = get_portais()
    
    for id_portal, nome, url, abrangencia, apelido in portais:
        pasta = criar_pasta(abrangencia)
        spider_code = gerar_spider_code(id_portal, nome, url, apelido)
        
        spider_path = os.path.join(pasta, f"{apelido}.py")
        with open(spider_path, "w", encoding="utf-8") as f:
            f.write(spider_code)
        
        print(f"Spider criado: {spider_path}")

if __name__ == "__main__":
    criar_spiders()
