import scrapy

class BalcaonewsSpider(scrapy.Spider):
    name = "Balcão News"
    ID = 232
    allowed_domains = ["balcaonews.com.br"]
    start_urls = ["https://balcaonews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
