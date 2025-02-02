import scrapy

class AlmgSpider(scrapy.Spider):
    name = "ALMG"
    ID = 82
    allowed_domains = ["www.almg.gov.br"]
    start_urls = ["https://www.almg.gov.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
