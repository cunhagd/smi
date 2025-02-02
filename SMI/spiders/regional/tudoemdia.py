import scrapy

class TudoemdiaSpider(scrapy.Spider):
    name = "Tudo em Dia"
    ID = 68
    allowed_domains = ["www.tudoemdia.com"]
    start_urls = ["https://www.tudoemdia.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
