import scrapy

class Correio_mgSpider(scrapy.Spider):
    name = "Correio de Minas (MG)"
    ID = 3
    allowed_domains = ["correiodeminas.com.br"]
    start_urls = ["https://correiodeminas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
