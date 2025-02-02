import scrapy

class PatosjaSpider(scrapy.Spider):
    name = "Patos Já"
    ID = 110
    allowed_domains = ["www.patosja.com.br"]
    start_urls = ["https://www.patosja.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
