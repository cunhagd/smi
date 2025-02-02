import scrapy

class JornalggnSpider(scrapy.Spider):
    name = "Jornal GGN"
    ID = 162
    allowed_domains = ["jornalggn.com.br"]
    start_urls = ["https://jornalggn.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
