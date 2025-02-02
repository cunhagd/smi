import scrapy

class OalfenenseSpider(scrapy.Spider):
    name = "O Alfenense"
    ID = 117
    allowed_domains = ["www.oalfenense.com.br"]
    start_urls = ["https://www.oalfenense.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
