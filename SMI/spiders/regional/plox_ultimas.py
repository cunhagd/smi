import scrapy

class Plox_ultimasSpider(scrapy.Spider):
    name = "Plox Últimas"
    ID = 6
    allowed_domains = ["plox.com.br"]
    start_urls = ["https://plox.com.br/ipatinga/ultimas-noticias"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
