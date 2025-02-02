import scrapy

class G1_coesteSpider(scrapy.Spider):
    name = "G1 Centro Oeste"
    ID = 234
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/centro-oeste/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
