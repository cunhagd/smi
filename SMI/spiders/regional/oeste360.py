import scrapy

class Oeste360Spider(scrapy.Spider):
    name = "Poder Oeste360"
    ID = 116
    allowed_domains = ["www.oeste360.com"]
    start_urls = ["https://www.oeste360.com/politica#google_vignette"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
