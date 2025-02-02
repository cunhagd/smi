import scrapy

class CafemutucaSpider(scrapy.Spider):
    name = "Café Mutuca"
    ID = 200
    allowed_domains = ["cafemutuca.com.br"]
    start_urls = ["https://cafemutuca.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
