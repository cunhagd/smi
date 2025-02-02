import scrapy

class Radio98Spider(scrapy.Spider):
    name = "Rádio 98FM"
    ID = 85
    allowed_domains = ["www.98live.com.br"]
    start_urls = ["https://www.98live.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
