import scrapy

class OpniaocaeteSpider(scrapy.Spider):
    name = "Opnião Caeté"
    ID = 118
    allowed_domains = ["www.opiniaocaete.com.br"]
    start_urls = ["https://www.opiniaocaete.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
