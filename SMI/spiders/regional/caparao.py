import scrapy

class CaparaoSpider(scrapy.Spider):
    name = "Portal Caparaó"
    ID = 198
    allowed_domains = ["www.portalcaparao.com.br"]
    start_urls = ["https://www.portalcaparao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
