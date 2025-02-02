import scrapy

class EsquerdadiarioSpider(scrapy.Spider):
    name = "Esquerda Diário"
    ID = 179
    allowed_domains = ["www.esquerdadiario.com.br"]
    start_urls = ["https://www.esquerdadiario.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
