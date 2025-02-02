import scrapy

class Ermida_mgSpider(scrapy.Spider):
    name = "Ermida MG"
    ID = 180
    allowed_domains = ["ermidamg.com"]
    start_urls = ["https://ermidamg.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
