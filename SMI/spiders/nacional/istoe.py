import scrapy

class IstoeSpider(scrapy.Spider):
    name = "Revista Isto É"
    ID = 46
    allowed_domains = ["istoe.com.br"]
    start_urls = ["https://istoe.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
