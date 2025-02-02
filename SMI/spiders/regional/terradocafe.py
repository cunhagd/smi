import scrapy

class TerradocafeSpider(scrapy.Spider):
    name = "Terra do Café"
    ID = 259
    allowed_domains = ["www.aterradocafe.com.br"]
    start_urls = ["https://www.aterradocafe.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
