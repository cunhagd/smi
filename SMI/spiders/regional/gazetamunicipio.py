import scrapy

class GazetamunicipioSpider(scrapy.Spider):
    name = "Gazeta dos Municípios"
    ID = 173
    allowed_domains = ["gazetadosmunicipios.com.br"]
    start_urls = ["https://gazetadosmunicipios.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
