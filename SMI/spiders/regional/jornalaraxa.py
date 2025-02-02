import scrapy

class JornalaraxaSpider(scrapy.Spider):
    name = "Jornal Araxá"
    ID = 147
    allowed_domains = ["jornalaraxa.com.br"]
    start_urls = ["https://jornalaraxa.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
