import scrapy

class CentrodomundoSpider(scrapy.Spider):
    name = "Diário Centro do Mundo"
    ID = 188
    allowed_domains = ["www.diariodocentrodomundo.com.br"]
    start_urls = ["https://www.diariodocentrodomundo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
