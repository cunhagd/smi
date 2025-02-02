import scrapy

class ItabiranetSpider(scrapy.Spider):
    name = "Itabira Net"
    ID = 153
    allowed_domains = ["itabiranet.com.br"]
    start_urls = ["https://itabiranet.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
