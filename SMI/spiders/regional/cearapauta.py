import scrapy

class CearapautaSpider(scrapy.Spider):
    name = "Ceará em Pauta"
    ID = 261
    allowed_domains = ["cearaempauta.com.br"]
    start_urls = ["https://cearaempauta.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
