import scrapy

class JornalalefSpider(scrapy.Spider):
    name = "Jornal Alef"
    ID = 149
    allowed_domains = ["jornalalef.com.br"]
    start_urls = ["https://jornalalef.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
