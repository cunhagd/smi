import scrapy

class GrnewsSpider(scrapy.Spider):
    name = "GRNews"
    ID = 163
    allowed_domains = ["grnews.com.br"]
    start_urls = ["https://grnews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
