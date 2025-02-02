import scrapy

class Hjdia_mgSpider(scrapy.Spider):
    name = "Hoje em Dia (MG)"
    ID = 19
    allowed_domains = ["www.hojeemdia.com.br"]
    start_urls = ["https://www.hojeemdia.com.br/minas"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
