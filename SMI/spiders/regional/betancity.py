import scrapy

class BetancitySpider(scrapy.Spider):
    name = "Betan City"
    ID = 203
    allowed_domains = ["betancity.com.br"]
    start_urls = ["https://betancity.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
