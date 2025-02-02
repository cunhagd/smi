import scrapy

class ZonamnewsSpider(scrapy.Spider):
    name = "Zona da Mata News"
    ID = 63
    allowed_domains = ["www.zonadamatanews.com.br"]
    start_urls = ["https://www.zonadamatanews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
