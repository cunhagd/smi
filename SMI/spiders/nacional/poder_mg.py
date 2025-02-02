import scrapy

class Poder_mgSpider(scrapy.Spider):
    name = "Poder 360"
    ID = 27
    allowed_domains = ["www.poder360.com.br"]
    start_urls = ["https://www.poder360.com.br/tag/minas-gerais/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
