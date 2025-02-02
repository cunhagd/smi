import scrapy

class MgtododiaSpider(scrapy.Spider):
    name = "MG Todo Dia"
    ID = 125
    allowed_domains = ["mgtododia.com.br"]
    start_urls = ["https://mgtododia.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
