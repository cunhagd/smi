import scrapy

class FolhasetelagoasSpider(scrapy.Spider):
    name = "Folha de Sete Lagoas"
    ID = 178
    allowed_domains = ["folhadesetelagoas.com"]
    start_urls = ["https://folhadesetelagoas.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
