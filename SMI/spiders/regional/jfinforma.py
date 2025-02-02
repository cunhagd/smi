import scrapy

class JfinformaSpider(scrapy.Spider):
    name = "JF Informa"
    ID = 131
    allowed_domains = ["jfinforma.com"]
    start_urls = ["https://jfinforma.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
