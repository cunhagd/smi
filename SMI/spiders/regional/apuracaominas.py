import scrapy

class ApuracaominasSpider(scrapy.Spider):
    name = "Apuração Minas"
    ID = 214
    allowed_domains = ["www.apuracaominas.com"]
    start_urls = ["https://www.apuracaominas.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
