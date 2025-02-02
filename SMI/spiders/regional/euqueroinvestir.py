import scrapy

class EuqueroinvestirSpider(scrapy.Spider):
    name = "Eu Quero Investir"
    ID = 185
    allowed_domains = ["euqueroinvestir.com"]
    start_urls = ["https://euqueroinvestir.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
