import scrapy

class FatorSpider(scrapy.Spider):
    name = "O Fator"
    ID = 84
    allowed_domains = ["ofator.com.br"]
    start_urls = ["https://ofator.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
