import scrapy

class PoderSpider(scrapy.Spider):
    name = "Poder 360"
    ID = 26
    allowed_domains = ["www.poder360.com.br"]
    start_urls = ["https://www.poder360.com.br/poder-hoje/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
