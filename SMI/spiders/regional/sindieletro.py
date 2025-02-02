import scrapy

class SindieletroSpider(scrapy.Spider):
    name = "SindiEletro"
    ID = 107
    allowed_domains = ["sindieletromg.org.br"]
    start_urls = ["https://sindieletromg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
