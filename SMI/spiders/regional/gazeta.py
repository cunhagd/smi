import scrapy

class GazetaSpider(scrapy.Spider):
    name = "Gazeta do Povo"
    ID = 42
    allowed_domains = ["www.gazetadopovo.com.br"]
    start_urls = ["https://www.gazetadopovo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
