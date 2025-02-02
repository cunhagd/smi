import scrapy

class ItabiranoticiaSpider(scrapy.Spider):
    name = "Itabira Notícia"
    ID = 152
    allowed_domains = ["itabiranoticia.com.br"]
    start_urls = ["https://itabiranoticia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
