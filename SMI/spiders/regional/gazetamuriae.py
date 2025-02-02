import scrapy

class GazetamuriaeSpider(scrapy.Spider):
    name = "Gazeta de Muriaé"
    ID = 169
    allowed_domains = ["gazetademuriae.com.br"]
    start_urls = ["https://gazetademuriae.com.br/noticia/lista"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
