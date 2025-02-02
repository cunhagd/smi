import scrapy

class JornalfatorealSpider(scrapy.Spider):
    name = "Jornal Fato Real"
    ID = 140
    allowed_domains = ["fatoreal.com.br"]
    start_urls = ["https://fatoreal.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
