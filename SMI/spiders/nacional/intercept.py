import scrapy

class InterceptSpider(scrapy.Spider):
    name = "The Intercept"
    ID = 43
    allowed_domains = ["www.intercept.com.br"]
    start_urls = ["https://www.intercept.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
