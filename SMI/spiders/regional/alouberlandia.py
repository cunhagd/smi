import scrapy

class AlouberlandiaSpider(scrapy.Spider):
    name = "Alô Uberlândia"
    ID = 204
    allowed_domains = ["www.alouberlandia.com"]
    start_urls = ["https://www.alouberlandia.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
