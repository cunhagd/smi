import scrapy

class DentrodetudoSpider(scrapy.Spider):
    name = "Por Dentro de Tudo"
    ID = 89
    allowed_domains = ["pordentrodetudo.com.br"]
    start_urls = ["https://pordentrodetudo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
