import scrapy

class JornalintegracaoSpider(scrapy.Spider):
    name = "Jornal Integração (Leia Fácil)"
    ID = 245
    allowed_domains = ["leiafacil.com.br"]
    start_urls = ["https://leiafacil.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
