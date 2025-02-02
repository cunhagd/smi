import scrapy

class GloboSpider(scrapy.Spider):
    name = "Globo"
    ID = 9
    allowed_domains = ["globo.com"]
    start_urls = ["https://globo.com"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
