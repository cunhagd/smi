import scrapy

class DivinewsSpider(scrapy.Spider):
    name = "Divinews"
    ID = 221
    allowed_domains = ["divinews.com"]
    start_urls = ["https://divinews.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
