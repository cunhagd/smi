import scrapy

class ArenadenoticiasSpider(scrapy.Spider):
    name = "Jornal Arena de Notícias"
    ID = 146
    allowed_domains = ["arenadenoticias.com.br"]
    start_urls = ["https://arenadenoticias.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
