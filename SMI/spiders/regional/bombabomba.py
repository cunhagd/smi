import scrapy

class BombabombaSpider(scrapy.Spider):
    name = "Portal Bomba Bomba"
    ID = 202
    allowed_domains = ["bombabomba.com.br"]
    start_urls = ["https://bombabomba.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
