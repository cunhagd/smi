import scrapy

class MinasaconteceSpider(scrapy.Spider):
    name = "Minas Acontece"
    ID = 127
    allowed_domains = ["minasacontece.com.br"]
    start_urls = ["https://minasacontece.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
