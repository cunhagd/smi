import scrapy

class BandnewsSpider(scrapy.Spider):
    name = "Rádio Band News"
    ID = 47
    allowed_domains = ["www.band.uol.com.br"]
    start_urls = ["https://www.band.uol.com.br/bandnews-fm/noticias"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
