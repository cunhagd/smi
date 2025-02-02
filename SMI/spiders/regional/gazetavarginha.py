import scrapy

class GazetavarginhaSpider(scrapy.Spider):
    name = "Gazeta de Varginha"
    ID = 229
    allowed_domains = ["www.gazetadevarginha.com.br"]
    start_urls = ["https://www.gazetadevarginha.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
