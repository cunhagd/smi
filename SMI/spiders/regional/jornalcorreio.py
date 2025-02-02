import scrapy

class JornalcorreioSpider(scrapy.Spider):
    name = "Jornal Correio"
    ID = 262
    allowed_domains = ["portalcorreio.com.br"]
    start_urls = ["https://portalcorreio.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
