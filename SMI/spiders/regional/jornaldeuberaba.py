import scrapy

class JornaldeuberabaSpider(scrapy.Spider):
    name = "Jornal de Uberaba"
    ID = 142
    allowed_domains = ["www.jornaldeuberaba.com.br"]
    start_urls = ["https://www.jornaldeuberaba.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
