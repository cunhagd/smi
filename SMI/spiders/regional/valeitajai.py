import scrapy

class ValeitajaiSpider(scrapy.Spider):
    name = "Vale do Itajaí Notícias"
    ID = 255
    allowed_domains = ["valedoitajainoticias.com.br"]
    start_urls = ["https://valedoitajainoticias.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
