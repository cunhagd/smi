import scrapy

class EstadaoSpider(scrapy.Spider):
    name = "Estadão"
    ID = 29
    allowed_domains = ["www.estadao.com.br"]
    start_urls = ["https://www.estadao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
