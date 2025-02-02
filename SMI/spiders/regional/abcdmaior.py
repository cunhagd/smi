import scrapy

class AbcdmaiorSpider(scrapy.Spider):
    name = "ABCD Maior"
    ID = 216
    allowed_domains = ["abcdmaior.com.br"]
    start_urls = ["https://abcdmaior.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
