import scrapy

class GazetaoesteSpider(scrapy.Spider):
    name = "Gazeta do Oeste"
    ID = 166
    allowed_domains = ["g37.com.br"]
    start_urls = ["https://g37.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
