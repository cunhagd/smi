import scrapy

class Itatiaia_opSpider(scrapy.Spider):
    name = "Itatiaia Ouro Preto"
    ID = 242
    allowed_domains = ["www.itatiaia.com.br"]
    start_urls = ["https://www.itatiaia.com.br/ouropreto"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
