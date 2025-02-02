import scrapy

class HjdiaSpider(scrapy.Spider):
    name = "Hoje em Dia"
    ID = 20
    allowed_domains = ["www.hojeemdia.com.br"]
    start_urls = ["https://www.hojeemdia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
