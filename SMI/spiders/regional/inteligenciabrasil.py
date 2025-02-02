import scrapy

class InteligenciabrasilSpider(scrapy.Spider):
    name = "Inteligência Brasil"
    ID = 189
    allowed_domains = ["ibi.ong.br"]
    start_urls = ["https://ibi.ong.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
