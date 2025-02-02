import scrapy

class JornaldosvalesSpider(scrapy.Spider):
    name = "Jornal dos Vales"
    ID = 253
    allowed_domains = ["jornaldosvales.com.br"]
    start_urls = ["https://jornaldosvales.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
