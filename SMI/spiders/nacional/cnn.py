import scrapy

class CnnSpider(scrapy.Spider):
    name = "CNN"
    ID = 22
    allowed_domains = ["www.cnnbrasil.com.br"]
    start_urls = ["https://www.cnnbrasil.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
