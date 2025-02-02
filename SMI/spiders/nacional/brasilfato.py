import scrapy

class BrasilfatoSpider(scrapy.Spider):
    name = "Brasil de Fato"
    ID = 50
    allowed_domains = ["www.brasildefato.com.br"]
    start_urls = ["https://www.brasildefato.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
