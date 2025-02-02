import scrapy

class RecordSpider(scrapy.Spider):
    name = "R7"
    ID = 36
    allowed_domains = ["www.r7.com"]
    start_urls = ["https://www.r7.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
