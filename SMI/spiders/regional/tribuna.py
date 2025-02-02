import scrapy

class TribunaSpider(scrapy.Spider):
    name = "Tribuna de Minas"
    ID = 240
    allowed_domains = ["tribunademinas.com.br"]
    start_urls = ["https://tribunademinas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
