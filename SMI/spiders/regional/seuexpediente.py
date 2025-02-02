import scrapy

class SeuexpedienteSpider(scrapy.Spider):
    name = "Seu Expediente"
    ID = 93
    allowed_domains = ["seuexpediente.com.br"]
    start_urls = ["https://seuexpediente.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
