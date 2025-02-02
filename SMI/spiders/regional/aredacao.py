import scrapy

class AredacaoSpider(scrapy.Spider):
    name = "A Redação"
    ID = 215
    allowed_domains = ["www.aredacao.com.br"]
    start_urls = ["https://www.aredacao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
