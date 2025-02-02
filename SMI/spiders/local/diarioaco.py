import scrapy

class DiarioacoSpider(scrapy.Spider):
    name = "Diário do Aço"
    ID = 2
    allowed_domains = ["www.diariodoaco.com.br"]
    start_urls = ["https://www.diariodoaco.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
