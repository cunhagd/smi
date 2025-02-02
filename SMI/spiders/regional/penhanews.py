import scrapy

class PenhanewsSpider(scrapy.Spider):
    name = "Penha News SP"
    ID = 104
    allowed_domains = ["www.penhanews.com.br"]
    start_urls = ["https://www.penhanews.com.br/brasil"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
