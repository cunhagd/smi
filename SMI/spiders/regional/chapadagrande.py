import scrapy

class ChapadagrandeSpider(scrapy.Spider):
    name = "Chapada Grande"
    ID = 196
    allowed_domains = ["www.chapadagrande.com"]
    start_urls = ["https://www.chapadagrande.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
