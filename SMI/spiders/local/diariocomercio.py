import scrapy

class DiariocomercioSpider(scrapy.Spider):
    name = "Diário do Comércio"
    ID = 251
    allowed_domains = ["diariodocomercio.com.br"]
    start_urls = ["https://diariodocomercio.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
