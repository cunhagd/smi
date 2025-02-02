import scrapy

class JmonlineSpider(scrapy.Spider):
    name = "JM Online"
    ID = 150
    allowed_domains = ["jmonline.com.br"]
    start_urls = ["https://jmonline.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
