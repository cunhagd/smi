import scrapy

class DiariouberlandiaSpider(scrapy.Spider):
    name = "Diário de Uberlândia"
    ID = 190
    allowed_domains = ["diariodeuberlandia.com.br"]
    start_urls = ["https://diariodeuberlandia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
