import scrapy

class Uol_mgSpider(scrapy.Spider):
    name = "Portal UOL (MG)"
    ID = 14
    allowed_domains = ["noticias.uol.com.br"]
    start_urls = ["https://noticias.uol.com.br/minas-gerais/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
