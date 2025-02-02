import scrapy

class TvcbrasilSpider(scrapy.Spider):
    name = "TVC Brasil"
    ID = 98
    allowed_domains = ["tvcbrasil.com.br"]
    start_urls = ["https://tvcbrasil.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
