import scrapy

class FolhacentrosulSpider(scrapy.Spider):
    name = "Folha Centro Sul"
    ID = 183
    allowed_domains = ["folhacentrosul.com.br"]
    start_urls = ["https://folhacentrosul.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
