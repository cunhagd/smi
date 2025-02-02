import scrapy

class AgbrasilSpider(scrapy.Spider):
    name = "Agência Brasil"
    ID = 38
    allowed_domains = ["agenciabrasil.ebc.com.br"]
    start_urls = ["https://agenciabrasil.ebc.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
