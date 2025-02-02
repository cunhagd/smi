import scrapy

class UltimasformigaSpider(scrapy.Spider):
    name = "Últimas Notícias - Formiga"
    ID = 267
    allowed_domains = ["ultimasnoticias.inf.br"]
    start_urls = ["https://ultimasnoticias.inf.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
