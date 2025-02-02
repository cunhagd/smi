import scrapy

class PanoramicanewsSpider(scrapy.Spider):
    name = "Panoramica News"
    ID = 114
    allowed_domains = ["panoramicanews.com"]
    start_urls = ["https://panoramicanews.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
