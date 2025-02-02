import scrapy

class GuiamuriaeSpider(scrapy.Spider):
    name = "Guia Muriaé"
    ID = 167
    allowed_domains = ["www.guiamuriae.com.br"]
    start_urls = ["https://www.guiamuriae.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
