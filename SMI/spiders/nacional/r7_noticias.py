import scrapy

class R7_noticiasSpider(scrapy.Spider):
    name = "JR 24H"
    ID = 37
    allowed_domains = ["noticias.r7.com"]
    start_urls = ["https://noticias.r7.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
