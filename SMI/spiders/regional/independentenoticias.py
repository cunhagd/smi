import scrapy

class IndependentenoticiasSpider(scrapy.Spider):
    name = "Independente Notícias"
    ID = 154
    allowed_domains = ["www.portalindependentenoticia.com.br"]
    start_urls = ["https://www.portalindependentenoticia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
