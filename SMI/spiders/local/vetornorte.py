import scrapy

class VetornorteSpider(scrapy.Spider):
    name = "Vetor Norte"
    ID = 77
    allowed_domains = ["vetornortenoticias.com"]
    start_urls = ["https://vetornortenoticias.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
