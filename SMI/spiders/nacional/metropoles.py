import scrapy

class MetropolesSpider(scrapy.Spider):
    name = "Metrópoles"
    ID = 24
    allowed_domains = ["www.metropoles.com"]
    start_urls = ["https://www.metropoles.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
