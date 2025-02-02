import scrapy

class Nova93fmSpider(scrapy.Spider):
    name = "Nova 93FM"
    ID = 122
    allowed_domains = ["nova93fm.com.br"]
    start_urls = ["https://nova93fm.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
