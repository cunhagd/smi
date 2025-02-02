import scrapy

class Portal24hSpider(scrapy.Spider):
    name = "Portal 24 Horas"
    ID = 61
    allowed_domains = ["portaldenoticias24horas.com.br"]
    start_urls = ["https://portaldenoticias24horas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
