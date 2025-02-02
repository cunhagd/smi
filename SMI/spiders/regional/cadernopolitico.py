import scrapy

class CadernopoliticoSpider(scrapy.Spider):
    name = "Caderno Político"
    ID = 193
    allowed_domains = ["cadernopolitico.com"]
    start_urls = ["https://cadernopolitico.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
