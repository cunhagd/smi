import scrapy

class CidadenaredeSpider(scrapy.Spider):
    name = "Cidade na Rede"
    ID = 194
    allowed_domains = ["cidadenarede.net"]
    start_urls = ["https://cidadenarede.net/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
