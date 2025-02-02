import scrapy

class Otempo_ultimasSpider(scrapy.Spider):
    name = "O Tempo"
    ID = 4
    allowed_domains = ["www.otempo.com.br"]
    start_urls = ["https://www.otempo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
