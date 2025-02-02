import scrapy

class FolhavitoriaSpider(scrapy.Spider):
    name = "Folha Vitória"
    ID = 192
    allowed_domains = ["www.folhavitoria.com.br"]
    start_urls = ["https://www.folhavitoria.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
