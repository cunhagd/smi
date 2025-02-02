import scrapy

class PocosjaSpider(scrapy.Spider):
    name = "Portal Poços Já"
    ID = 16
    allowed_domains = ["pocosja.com.br"]
    start_urls = ["https://pocosja.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
