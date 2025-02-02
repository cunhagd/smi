import scrapy

class RegionalzaoSpider(scrapy.Spider):
    name = "Portal Regionalzão"
    ID = 136
    allowed_domains = ["regionalzao.com.br"]
    start_urls = ["https://regionalzao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
