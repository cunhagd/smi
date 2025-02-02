import scrapy

class Onda_sulSpider(scrapy.Spider):
    name = "Onda Sul"
    ID = 31
    allowed_domains = ["www.portalondasul.com.br"]
    start_urls = ["https://www.portalondasul.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
