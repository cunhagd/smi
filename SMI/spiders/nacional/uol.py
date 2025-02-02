import scrapy

class UolSpider(scrapy.Spider):
    name = "Portal UOL"
    ID = 15
    allowed_domains = ["www.uol.com.br"]
    start_urls = ["https://www.uol.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
