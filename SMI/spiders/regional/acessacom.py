import scrapy

class AcessacomSpider(scrapy.Spider):
    name = "Acessa.com"
    ID = 254
    allowed_domains = ["www.acessa.com"]
    start_urls = ["https://www.acessa.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
