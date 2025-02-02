import scrapy

class R7_mgSpider(scrapy.Spider):
    name = "R7 Minas Gerais"
    ID = 35
    allowed_domains = ["noticias.r7.com"]
    start_urls = ["https://noticias.r7.com/minas-gerais/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
