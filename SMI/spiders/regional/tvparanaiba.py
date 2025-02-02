import scrapy

class TvparanaibaSpider(scrapy.Spider):
    name = "TV Paranaíba"
    ID = 227
    allowed_domains = ["tvparanaiba.com.br"]
    start_urls = ["https://tvparanaiba.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
