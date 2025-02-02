import scrapy

class Itatiaia_ultimasSpider(scrapy.Spider):
    name = "Itatiaia (MG)"
    ID = 5
    allowed_domains = ["www.itatiaia.com.br"]
    start_urls = ["https://www.itatiaia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
