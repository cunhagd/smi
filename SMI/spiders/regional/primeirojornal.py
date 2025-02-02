import scrapy

class PrimeirojornalSpider(scrapy.Spider):
    name = "Primeiro Jornal"
    ID = 105
    allowed_domains = ["primeirojornal.com.br"]
    start_urls = ["https://primeirojornal.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
