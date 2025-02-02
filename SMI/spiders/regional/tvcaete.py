import scrapy

class TvcaeteSpider(scrapy.Spider):
    name = "TV Caeté"
    ID = 96
    allowed_domains = ["www.tvcaete.com.br"]
    start_urls = ["https://www.tvcaete.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
