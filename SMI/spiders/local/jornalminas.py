import scrapy

class JornalminasSpider(scrapy.Spider):
    name = "Jornal Minas"
    ID = 74
    allowed_domains = ["jornalminas.com.br"]
    start_urls = ["https://jornalminas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
