import scrapy

class FolhapatenseSpider(scrapy.Spider):
    name = "Folha Patense"
    ID = 175
    allowed_domains = ["www.folhapatense.com.br"]
    start_urls = ["https://www.folhapatense.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
