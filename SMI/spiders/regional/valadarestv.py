import scrapy

class ValadarestvSpider(scrapy.Spider):
    name = "Valadares na TV"
    ID = 66
    allowed_domains = ["valadaresnatv.com.br"]
    start_urls = ["https://valadaresnatv.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
