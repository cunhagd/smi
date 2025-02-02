import scrapy

class OgloboSpider(scrapy.Spider):
    name = "Portal O Globo"
    ID = 13
    allowed_domains = ["oglobo.globo.com"]
    start_urls = ["https://oglobo.globo.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
