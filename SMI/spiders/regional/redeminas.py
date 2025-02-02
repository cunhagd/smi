import scrapy

class RedeminasSpider(scrapy.Spider):
    name = "RedeMinas TV"
    ID = 100
    allowed_domains = ["redeminas.tv"]
    start_urls = ["https://redeminas.tv/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
