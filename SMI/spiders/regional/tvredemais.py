import scrapy

class TvredemaisSpider(scrapy.Spider):
    name = "TV Rede Mais"
    ID = 226
    allowed_domains = ["redemais.tv.br"]
    start_urls = ["https://redemais.tv.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
