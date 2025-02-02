import scrapy

class PrimeirapaginaSpider(scrapy.Spider):
    name = "Primeira Página"
    ID = 88
    allowed_domains = ["primeirapagina.com.br"]
    start_urls = ["https://primeirapagina.com.br/mato-grosso/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
