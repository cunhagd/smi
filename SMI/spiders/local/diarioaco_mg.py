import scrapy

class Diarioaco_mgSpider(scrapy.Spider):
    name = "Diário do Aço (MG)"
    ID = 1
    allowed_domains = ["www.diariodoaco.com.br"]
    start_urls = ["https://www.diariodoaco.com.br/minas"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
