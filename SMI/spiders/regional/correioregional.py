import scrapy

class CorreioregionalSpider(scrapy.Spider):
    name = "Correio Regional"
    ID = 143
    allowed_domains = ["correioregional.net"]
    start_urls = ["https://correioregional.net/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
