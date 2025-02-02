import scrapy

class Band_mgSpider(scrapy.Spider):
    name = "Portal Band Minas"
    ID = 17
    allowed_domains = ["www.band.uol.com.br"]
    start_urls = ["https://www.band.uol.com.br/minas-gerais"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
