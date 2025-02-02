import scrapy

class BarrosoemdiaSpider(scrapy.Spider):
    name = "Barroso em Dia"
    ID = 231
    allowed_domains = ["barrosoemdia.com.br"]
    start_urls = ["https://barrosoemdia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
