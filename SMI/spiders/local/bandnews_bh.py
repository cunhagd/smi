import scrapy

class Bandnews_bhSpider(scrapy.Spider):
    name = "Rádio Band News (BH)"
    ID = 48
    allowed_domains = ["www.band.uol.com.br"]
    start_urls = ["https://www.band.uol.com.br/bandnews-fm/belo-horizonte"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
