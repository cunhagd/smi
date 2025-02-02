import scrapy

class HoradopovoSpider(scrapy.Spider):
    name = "Portal Hora do Povo"
    ID = 158
    allowed_domains = ["horadopovo.com.br"]
    start_urls = ["https://horadopovo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
