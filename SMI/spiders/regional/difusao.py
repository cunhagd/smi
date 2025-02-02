import scrapy

class DifusaoSpider(scrapy.Spider):
    name = "Portal Difusao Brasil"
    ID = 144
    allowed_domains = ["www.difusaobrasil.com.br"]
    start_urls = ["https://www.difusaobrasil.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
