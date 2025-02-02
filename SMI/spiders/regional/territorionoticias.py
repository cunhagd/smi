import scrapy

class TerritorionoticiasSpider(scrapy.Spider):
    name = "Território Notícias"
    ID = 70
    allowed_domains = ["territoriopress.com.br"]
    start_urls = ["https://territoriopress.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
