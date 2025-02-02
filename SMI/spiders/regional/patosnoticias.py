import scrapy

class PatosnoticiasSpider(scrapy.Spider):
    name = "Patos Notícias"
    ID = 90
    allowed_domains = ["patosnoticias.com.br"]
    start_urls = ["https://patosnoticias.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
