import scrapy

class JornalvozativaSpider(scrapy.Spider):
    name = "Jornal Voz Ativa"
    ID = 134
    allowed_domains = ["jornalvozativa.com"]
    start_urls = ["https://jornalvozativa.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
