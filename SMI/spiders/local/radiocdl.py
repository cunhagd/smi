import scrapy

class RadiocdlSpider(scrapy.Spider):
    name = "Rádio CDL FM"
    ID = 75
    allowed_domains = ["cdlfm.com.br"]
    start_urls = ["https://cdlfm.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
