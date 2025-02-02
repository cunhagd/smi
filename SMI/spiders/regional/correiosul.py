import scrapy

class CorreiosulSpider(scrapy.Spider):
    name = "Portal Correio do Sul"
    ID = 199
    allowed_domains = ["portalc1.com.br"]
    start_urls = ["https://portalc1.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
