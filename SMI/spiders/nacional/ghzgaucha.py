import scrapy

class GhzgauchaSpider(scrapy.Spider):
    name = "GHZ Gaucha"
    ID = 56
    allowed_domains = ["gauchazh.clicrbs.com.br"]
    start_urls = ["https://gauchazh.clicrbs.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
