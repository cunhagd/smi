import scrapy

class SindepominasSpider(scrapy.Spider):
    name = "SindepoMinas"
    ID = 109
    allowed_domains = ["www.sindepominas.com.br"]
    start_urls = ["https://www.sindepominas.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
