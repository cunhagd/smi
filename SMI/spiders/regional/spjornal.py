import scrapy

class SpjornalSpider(scrapy.Spider):
    name = "São Paulo Jornal"
    ID = 86
    allowed_domains = ["saopaulojornal.com.br"]
    start_urls = ["https://saopaulojornal.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
