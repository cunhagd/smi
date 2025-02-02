import scrapy

class Gp1Spider(scrapy.Spider):
    name = "Portal GP1"
    ID = 161
    allowed_domains = ["www.gp1.com.br"]
    start_urls = ["https://www.gp1.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
