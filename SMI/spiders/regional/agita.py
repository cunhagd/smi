import scrapy

class AgitaSpider(scrapy.Spider):
    name = "Portal Agita"
    ID = 206
    allowed_domains = ["portalagita.com.br"]
    start_urls = ["https://portalagita.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
