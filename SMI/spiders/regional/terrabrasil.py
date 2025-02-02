import scrapy

class TerrabrasilSpider(scrapy.Spider):
    name = "Terra Brasil Notícias"
    ID = 69
    allowed_domains = ["terrabrasilnoticias.com"]
    start_urls = ["https://terrabrasilnoticias.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
