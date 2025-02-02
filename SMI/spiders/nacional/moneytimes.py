import scrapy

class MoneytimesSpider(scrapy.Spider):
    name = "Money Times"
    ID = 59
    allowed_domains = ["www.moneytimes.com.br"]
    start_urls = ["https://www.moneytimes.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
