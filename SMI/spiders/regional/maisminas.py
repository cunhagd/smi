import scrapy

class MaisminasSpider(scrapy.Spider):
    name = "Jornal Mais Minas"
    ID = 268
    allowed_domains = ["jornalmaisminas.com.br"]
    start_urls = ["https://jornalmaisminas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
