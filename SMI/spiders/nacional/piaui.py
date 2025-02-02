import scrapy

class PiauiSpider(scrapy.Spider):
    name = "Revista Piauí"
    ID = 60
    allowed_domains = ["piaui.folha.uol.com.br"]
    start_urls = ["https://piaui.folha.uol.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
