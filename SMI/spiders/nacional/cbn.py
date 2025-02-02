import scrapy

class CbnSpider(scrapy.Spider):
    name = "Rádio CBN Nacional"
    ID = 49
    allowed_domains = ["cbn.globo.com"]
    start_urls = ["https://cbn.globo.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
