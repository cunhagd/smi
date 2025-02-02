import scrapy

class Difusora95fmSpider(scrapy.Spider):
    name = "Difusora 95 FM"
    ID = 222
    allowed_domains = ["difusora95.com.br"]
    start_urls = ["https://difusora95.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
