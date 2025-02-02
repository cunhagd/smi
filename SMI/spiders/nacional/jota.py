import scrapy

class JotaSpider(scrapy.Spider):
    name = "Jota"
    ID = 53
    allowed_domains = ["www.jota.info"]
    start_urls = ["https://www.jota.info/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
