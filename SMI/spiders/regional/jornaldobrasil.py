import scrapy

class JornaldobrasilSpider(scrapy.Spider):
    name = "Jornal do Brasil"
    ID = 151
    allowed_domains = ["www.jb.com.br"]
    start_urls = ["https://www.jb.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
