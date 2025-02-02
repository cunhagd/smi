import scrapy

class TonamidiaSpider(scrapy.Spider):
    name = "To na Mídia"
    ID = 67
    allowed_domains = ["tonamidia.com.br"]
    start_urls = ["https://tonamidia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
