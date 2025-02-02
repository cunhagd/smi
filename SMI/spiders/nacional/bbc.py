import scrapy

class BbcSpider(scrapy.Spider):
    name = "Portal BBC"
    ID = 39
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/portuguese"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
