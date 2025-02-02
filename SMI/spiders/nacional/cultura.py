import scrapy

class CulturaSpider(scrapy.Spider):
    name = "TV Cultura"
    ID = 18
    allowed_domains = ["cultura.uol.com.br"]
    start_urls = ["https://cultura.uol.com.br/eleicoes/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
