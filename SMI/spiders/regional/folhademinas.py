import scrapy

class FolhademinasSpider(scrapy.Spider):
    name = "O Folha de Minas"
    ID = 266
    allowed_domains = ["ofolhademinas.com.br"]
    start_urls = ["https://ofolhademinas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
