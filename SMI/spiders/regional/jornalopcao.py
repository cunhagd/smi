import scrapy

class JornalopcaoSpider(scrapy.Spider):
    name = "Jornal Opção"
    ID = 265
    allowed_domains = ["www.jornalopcao.com.br"]
    start_urls = ["https://www.jornalopcao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
