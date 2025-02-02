import scrapy

class MpaSpider(scrapy.Spider):
    name = "Sistema MPA"
    ID = 263
    allowed_domains = ["www.sistemampa.com.br"]
    start_urls = ["https://www.sistemampa.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
