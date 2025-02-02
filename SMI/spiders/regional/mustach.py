import scrapy

class MustachSpider(scrapy.Spider):
    name = "Mustach"
    ID = 123
    allowed_domains = ["www.mustach.com.br"]
    start_urls = ["https://www.mustach.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
