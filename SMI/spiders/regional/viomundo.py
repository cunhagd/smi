import scrapy

class ViomundoSpider(scrapy.Spider):
    name = "Vi o Mundo"
    ID = 65
    allowed_domains = ["www.viomundo.com.br"]
    start_urls = ["https://www.viomundo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
