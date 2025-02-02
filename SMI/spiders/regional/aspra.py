import scrapy

class AspraSpider(scrapy.Spider):
    name = "Portal Aspra"
    ID = 210
    allowed_domains = ["aspra.org.br"]
    start_urls = ["https://aspra.org.br/portal/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
