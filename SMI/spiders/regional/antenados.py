import scrapy

class AntenadosSpider(scrapy.Spider):
    name = "Portal Antenados"
    ID = 208
    allowed_domains = ["portalantenados.com.br"]
    start_urls = ["https://portalantenados.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
