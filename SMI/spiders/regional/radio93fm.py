import scrapy

class Radio93fmSpider(scrapy.Spider):
    name = "Rádio 93 FM"
    ID = 224
    allowed_domains = ["radio93.com.br"]
    start_urls = ["https://radio93.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
