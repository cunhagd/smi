import scrapy

class VitoriosaSpider(scrapy.Spider):
    name = "Vitoriosa 9"
    ID = 64
    allowed_domains = ["v9vitoriosa.com.br"]
    start_urls = ["https://v9vitoriosa.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
