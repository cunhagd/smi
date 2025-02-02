import scrapy

class NoticiaonlineSpider(scrapy.Spider):
    name = "A Notícia Online"
    ID = 211
    allowed_domains = ["anoticiaregional.com.br"]
    start_urls = ["https://anoticiaregional.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
