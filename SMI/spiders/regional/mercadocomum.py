import scrapy

class MercadocomumSpider(scrapy.Spider):
    name = "Mecado Comum"
    ID = 92
    allowed_domains = ["mercadocomum.com"]
    start_urls = ["https://mercadocomum.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
