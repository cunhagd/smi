import scrapy

class Aqui_mgSpider(scrapy.Spider):
    name = "Aqui (MG)"
    ID = 28
    allowed_domains = ["aqui.uai.com.br"]
    start_urls = ["https://aqui.uai.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
