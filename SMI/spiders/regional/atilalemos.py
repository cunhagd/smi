import scrapy

class AtilalemosSpider(scrapy.Spider):
    name = "Átila Lemos"
    ID = 233
    allowed_domains = ["atilalemos.com.br"]
    start_urls = ["https://atilalemos.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
