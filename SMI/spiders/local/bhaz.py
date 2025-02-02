import scrapy

class BhazSpider(scrapy.Spider):
    name = "BHAZ"
    ID = 264
    allowed_domains = ["bhaz.com.br"]
    start_urls = ["https://bhaz.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
