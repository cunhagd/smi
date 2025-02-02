import scrapy

class Cnn_mgSpider(scrapy.Spider):
    name = "CNN (MG)"
    ID = 23
    allowed_domains = ["www.cnnbrasil.com.br"]
    start_urls = ["https://www.cnnbrasil.com.br/tudo-sobre/minas-gerais/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
