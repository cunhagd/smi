import scrapy

class Alterosa_znmataSpider(scrapy.Spider):
    name = "TV Alterosa - Zona da Mata"
    ID = 246
    allowed_domains = ["www.alterosa.com.br"]
    start_urls = ["https://www.alterosa.com.br/programas/alterosa-em-alerta-zona-da-mata/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
