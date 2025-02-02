import scrapy

class SmpnovalimaSpider(scrapy.Spider):
    name = "Sempre Nova Lima"
    ID = 76
    allowed_domains = ["semprenovalima.com"]
    start_urls = ["https://semprenovalima.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
