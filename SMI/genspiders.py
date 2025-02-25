import os
import sqlite3

# Caminho do banco de dados
DB_PATH = r"C:\Users\m1603994\SMI\db\banco_smi.db"
BASE_DIR = r"C:\Users\m1603994\SMI\SMI\spiders"

# Conectar ao banco de dados
def get_portais():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, apelido, abrangencia FROM portais")  # Corrigido aqui
    portais = cursor.fetchall()
    conn.close()
    return portais

# Criar estrutura de diretórios
def criar_pasta(abrangencia):
    pasta = os.path.join(BASE_DIR, abrangencia.lower())
    os.makedirs(pasta, exist_ok=True)
    return pasta

# Gerar código base do spider
def gerar_spider_code(nome):
    return f'''from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.database import buscar_urls, buscar_apelido, buscar_pontos, buscar_abrangencia, buscar_categorias, seletor_autor, seletor_corpo, DB_PATH
from SMI.items import NoticiaItem
from SMI.utils import filtrar_keywords
class EmSpider(SitemapSpider):
    name = "{nome}"
    def __init__(self, *args, **kwargs):
        super(EmSpider, self).__init__(*args, **kwargs)
        apelidos = buscar_apelido(self.name)
        if apelidos:
            self.sitemap_urls = buscar_urls(DB_PATH, apelidos[0])
        else:
            print("Nenhum apelido encontrado no banco de dados.")
            self.sitemap_urls = []
        self.categorias_indesejadas = set(buscar_categorias())
    def obter_seletor(self, funcao_seletor, tipo):
        seletor = funcao_seletor(DB_PATH, self.name)
        if not seletor:
            self.log(f"Seletor CSS para {tipo} não encontrado para o portal '{self.name}'")
            return None
        return seletor
    def parse(self, response):
        current_timestamp = datetime.now().isoformat()
        today = datetime.now().date()
        # Ignora URLs com categorias indesejadas
        if any(categoria in response.url for categoria in self.categorias_indesejadas):
            self.logger.info(f"URL ignorada (categoria indesejada): {response.url}")
            return
        # Extrai o título da notícia
        title = response.xpath('//title/text()').get()
        if not title:
            title = response.xpath('//h1/text()').get()
        if not title:
            title = response.xpath('//meta[@property="og:title"]/@content').get()
        # Cria o objeto NoticiaItem
        item = NoticiaItem()
        item['title'] = title
        item['timestamp'] = current_timestamp
        item['url'] = response.url
        # Verifica se a notícia é de hoje
        news_date = datetime.fromisoformat(item["timestamp"]).date()
        if news_date != today:
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")
            return
        # Obtém o seletor do corpo da notícia
        sel_corpo = self.obter_seletor(seletor_corpo, "corpo")
        if not sel_corpo:
            return
        # Extrai o corpo completo da notícia
        paragrafos = response.css(sel_corpo).getall()
        corpo_completo = "\n".join([p.strip() for p in paragrafos if p.strip()])
        item['corpo_completo'] = corpo_completo
        # Filtra a notícia com base nas palavras-chave
        palavras_encontradas = filtrar_keywords(DB_PATH, corpo_completo, debug=True)
        if not palavras_encontradas:
            self.log(f"Notícia ignorada (não atende às palavras-chave): {response.url}")
            return
        # Verifica a regra de relevância
        tem_obrigatoria = len(palavras_encontradas["obrigatorias"]) > 0
        tem_adicional = len(palavras_encontradas["adicionais"]) > 0
        if not (tem_obrigatoria and tem_adicional):
            self.log(f"Notícia ignorada (não atende à regra de relevância): {response.url}")
            return
        # Adiciona as palavras-chave encontradas ao item
        item['palavras_obrigatorias_encontradas'] = palavras_encontradas["obrigatorias"]
        item['palavras_adicionais_encontradas'] = palavras_encontradas["adicionais"]
        # Extrai o autor usando o seletor obtido
        sel_autor = self.obter_seletor(seletor_autor, "autor")
        if sel_autor:
            autor_element = response.css(sel_autor).get()  # Obtém o elemento HTML
            if autor_element:
                # Extrai apenas o texto do elemento
                autor = response.css(sel_autor + '::text').get()
                item['autor'] = autor.strip() if autor else None
            else:
                item['autor'] = None
        # Busca pontos e abrangência do portal
        pontos_portal = buscar_pontos(self.name)
        item['pontos'] = pontos_portal if pontos_portal else None
        abrangencia_portal = buscar_abrangencia(self.name)
        item['abrangencia'] = abrangencia_portal if abrangencia_portal else None
        # Retorna o item da notícia
        yield item
'''

# Criar spiders automaticamente
def criar_spiders():
    os.makedirs(BASE_DIR, exist_ok=True)  # Garante que a pasta spiders principal seja criada
    portais = get_portais()
    
    for nome, apelido, abrangencia in portais:  # Agora funciona corretamente
        pasta = criar_pasta(abrangencia)
        spider_code = gerar_spider_code(nome)
        
        spider_path = os.path.join(pasta, f"{apelido}.py")
        with open(spider_path, "w", encoding="utf-8") as f:
            f.write(spider_code)
        
        print(f"Spider criado: {spider_path}")

if __name__ == "__main__":
    criar_spiders()