import scrapy

class G1_zmataSpider(scrapy.Spider):
    name = "G1 Zona da Mata"
    ID = 239
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/zona-da-mata/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
