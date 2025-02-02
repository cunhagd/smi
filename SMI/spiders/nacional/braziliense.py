import scrapy

class BrazilienseSpider(scrapy.Spider):
    name = "Correio Braziliense"
    ID = 30
    allowed_domains = ["www.correiobraziliense.com.br"]
    start_urls = ["https://www.correiobraziliense.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
