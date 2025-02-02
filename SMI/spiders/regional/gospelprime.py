import scrapy

class GospelprimeSpider(scrapy.Spider):
    name = "Gospel Prime"
    ID = 160
    allowed_domains = ["www.gospelprime.com.br"]
    start_urls = ["https://www.gospelprime.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
