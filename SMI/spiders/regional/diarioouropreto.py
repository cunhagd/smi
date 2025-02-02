import scrapy

class DiarioouropretoSpider(scrapy.Spider):
    name = "Diário de Ouro Preto"
    ID = 186
    allowed_domains = ["www.diariodeouropreto.com.br"]
    start_urls = ["https://www.diariodeouropreto.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
