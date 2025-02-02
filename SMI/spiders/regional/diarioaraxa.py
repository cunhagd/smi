import scrapy

class DiarioaraxaSpider(scrapy.Spider):
    name = "Diário de Araxá"
    ID = 249
    allowed_domains = ["www.diariodearaxa.com.br"]
    start_urls = ["https://www.diariodearaxa.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
