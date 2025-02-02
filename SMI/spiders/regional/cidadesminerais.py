import scrapy

class CidadesmineraisSpider(scrapy.Spider):
    name = "Cidades e Minerais"
    ID = 230
    allowed_domains = ["cidadeseminerais.com.br"]
    start_urls = ["https://cidadeseminerais.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
