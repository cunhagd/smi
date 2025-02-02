import scrapy

class DefatoonlineSpider(scrapy.Spider):
    name = "Defato Online"
    ID = 174
    allowed_domains = ["defatoonline.com.br"]
    start_urls = ["https://defatoonline.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
