import scrapy

class VamosadianteSpider(scrapy.Spider):
    name = "Vamos Adiante"
    ID = 99
    allowed_domains = ["vamosadiante.com.br"]
    start_urls = ["https://vamosadiante.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
