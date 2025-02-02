import scrapy

class EsbrasilSpider(scrapy.Spider):
    name = "ES Brasil"
    ID = 184
    allowed_domains = ["esbrasil.com.br"]
    start_urls = ["https://esbrasil.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
