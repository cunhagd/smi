import scrapy

class SenadoSpider(scrapy.Spider):
    name = "Senado"
    ID = 57
    allowed_domains = ["www12.senado.leg.br"]
    start_urls = ["https://www12.senado.leg.br/noticias"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
