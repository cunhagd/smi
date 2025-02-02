import scrapy

class Band_uolSpider(scrapy.Spider):
    name = "Band Uol"
    ID = 33
    allowed_domains = ["www.band.uol.com.br"]
    start_urls = ["https://www.band.uol.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
