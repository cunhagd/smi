import scrapy

class Sinmed_mgSpider(scrapy.Spider):
    name = "Sinmed MG"
    ID = 252
    allowed_domains = ["sinmedmg.org.br"]
    start_urls = ["https://sinmedmg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
