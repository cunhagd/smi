import scrapy

class Record_newsSpider(scrapy.Spider):
    name = "Record News"
    ID = 34
    allowed_domains = ["noticias.r7.com"]
    start_urls = ["https://noticias.r7.com/record-news/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
