import scrapy

class MpmgSpider(scrapy.Spider):
    name = "MPMG"
    ID = 79
    allowed_domains = ["www.mpmg.mp.br"]
    start_urls = ["https://www.mpmg.mp.br/portal/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
