import scrapy

class ObrasilianistapoliSpider(scrapy.Spider):
    name = "O Brasilianista"
    ID = 120
    allowed_domains = ["obrasilianista.com.br"]
    start_urls = ["https://obrasilianista.com.br"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
