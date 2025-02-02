import scrapy

class CamaraSpider(scrapy.Spider):
    name = "Câmara Federal"
    ID = 55
    allowed_domains = ["www.camara.leg.br"]
    start_urls = ["https://www.camara.leg.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
