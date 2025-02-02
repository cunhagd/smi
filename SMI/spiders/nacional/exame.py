import scrapy

class ExameSpider(scrapy.Spider):
    name = "Revista Exame"
    ID = 45
    allowed_domains = ["exame.com"]
    start_urls = ["https://exame.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
