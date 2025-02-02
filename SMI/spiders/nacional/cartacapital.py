import scrapy

class CartacapitalSpider(scrapy.Spider):
    name = "Brasil de Fato"
    ID = 51
    allowed_domains = ["www.cartacapital.com.br"]
    start_urls = ["https://www.cartacapital.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
