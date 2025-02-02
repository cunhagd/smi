import scrapy

class FolhaSpider(scrapy.Spider):
    name = "Folha de SP"
    ID = 44
    allowed_domains = ["www1.folha.uol.com.br"]
    start_urls = ["https://www1.folha.uol.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
