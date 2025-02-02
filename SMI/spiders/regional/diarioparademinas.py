import scrapy

class DiarioparademinasSpider(scrapy.Spider):
    name = "Jornal Diário de Pará de Minas"
    ID = 141
    allowed_domains = ["www.jdiario.com.br"]
    start_urls = ["https://www.jdiario.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
