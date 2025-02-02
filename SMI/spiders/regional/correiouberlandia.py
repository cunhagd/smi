import scrapy

class CorreiouberlandiaSpider(scrapy.Spider):
    name = "Correo de Uberlândia"
    ID = 201
    allowed_domains = ["jornalcorreiodeuberlandia.com.br"]
    start_urls = ["https://jornalcorreiodeuberlandia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
