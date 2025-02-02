import scrapy

class BairrosnetSpider(scrapy.Spider):
    name = "Jornal Bairros Net"
    ID = 145
    allowed_domains = ["www.jornalbairrosnet.com.br"]
    start_urls = ["https://www.jornalbairrosnet.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
